from typing import Dict, Any, Union

from graphviz import Graph, Digraph

from coauthors_search.structures import Tree
from coauthors_search.structures import Author, AuthorCredentials
from coauthors_search.utils import Fetch


def generate_graph(tree: Tree, target: Author, configuration: Dict[str, Any]):
    graph = None

    if configuration['graph_type'] == 'directed':
        graph = Digraph("Authors")
    else:
        graph = Graph("Authors")

    try:
        graph.format = configuration['format']
    except KeyError:
        ...

    additional_nodes_limit = 0
    try:
        additional_nodes_limit = configuration['additional_nodes']
    except KeyError:
        ...

    main_branch_color = "BLACK"
    try:
        main_branch_color = configuration['main_branch_color']
    except KeyError:
        ...

    additional_branch_color = "BLACK"
    try:
        additional_branch_color = configuration['additional_branch_color']
    except KeyError:
        ...

    main_branch = tree.tree[target.id]
    previous_node = None
    nodes = []

    for node in main_branch:
        Fetch.fetch_image(node)
        additional_nodes = 0
        nodes.append(node.id)

        for additional_node in node.coauthors:
            if additional_node.id not in nodes and additional_nodes <= additional_nodes_limit and additional_node not in main_branch:
                if isinstance(additional_node, AuthorCredentials):
                    additional_node = additional_node._source.fetch_by_credentials(additional_node)
                Fetch.fetch_image(additional_node)
                additional_nodes += 1
                graph.node(
                    str(additional_node.id),
                    '',
                    {
                        'label': f"""<<TABLE border="0">
                        <TR>
                            <TD  bgcolor="white" border="0">{additional_node.get_short_name(10)}</TD>
                        </TR>
                        </TABLE>>""",
                        'image': f'images/{additional_node.id}.png',
                        'shape': 'plaintext',
                        'labelloc': 'b',
                        'fixedsize': 'true',
                        'width': '1',
                        'height': '1',
                        'imagescale': 'true',
                        'fontsize': '8',
                        'color': additional_branch_color
                    }
                )
                graph.edge(node.id, additional_node.id)
            else:
                break

        graph.node(
            str(node.id),
            '',
            {
                'label': f"""<<TABLE border="0">
                <TR>
                    <TD  bgcolor="white" border="0">{node.get_short_name(10)}</TD>
                </TR>
                </TABLE>>""",
                'image': f'images/{node.id}.png',
                'shape': 'plaintext',
                'labelloc': 'b',
                'fixedsize': 'true',
                'width': '1',
                'height': '1',
                'imagescale': 'true',
                'fontsize': '8',
                'color': main_branch_color
            }
        )

        if previous_node is not None:
            graph.edge(previous_node.id, node.id)
        previous_node = node

    graph.node('legend', '', {
        'label': f"""<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
             <TR>
              <TD COLSPAN="2"><B>Legend</B></TD>
             </TR>
             <TR>
              <TD>Main Branch</TD>
              <TD BGCOLOR="{main_branch_color}"></TD>
             </TR>
             <TR>
              <TD>Additional Branch</TD>
              <TD BGCOLOR="{additional_branch_color}"></TD>
             </TR>
            </TABLE>
           >""",
        'shape': 'plaintext',
    })

    graph.view(cleanup=True)
