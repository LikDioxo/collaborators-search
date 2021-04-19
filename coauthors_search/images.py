from typing import Dict, Any, Union

from graphviz import Graph, Digraph

from coauthors_search.structures import Tree
from coauthors_search.structures import Author, AuthorCredentials
from coauthors_search.utils import Fetch, validate_configuration


_REQUIREMENTS = ["graph_type", "image_path", "graph_path"]
_DEFAULT_CONFIGS = {
    "graph_name": "Authors",
    "format": "pdf",
    'additional_nodes': 0,
    'main_branch_color': "BLACK",
    'additional_branch_color': "BLACK"
}


@validate_configuration(_REQUIREMENTS, _DEFAULT_CONFIGS)
def generate_graph(tree: Tree, target: Author, *, configuration: Dict[str, Any]):
    if configuration['graph_type'] == 'directed':
        graph = Digraph("Authors")
    else:
        graph = Graph("Authors")
    img_path = configuration["image_path"]
    graph_path = configuration["graph_path"]
    graph_name = configuration["graph_name"]
    graph.format = configuration['format']
    additional_nodes_limit = configuration['additional_nodes']
    main_branch_color = configuration['main_branch_color']
    additional_branch_color = configuration['additional_branch_color']

    main_branch = tree.tree[target.id]
    previous_node = None
    nodes = []

    for node in main_branch:
        Fetch.fetch_image(node, img_path)
        additional_nodes = 0
        nodes.append(node.id)

        for additional_node in node.coauthors:
            if additional_node.id not in nodes and additional_nodes <= additional_nodes_limit and additional_node not in main_branch:
                if isinstance(additional_node, AuthorCredentials):
                    additional_node = additional_node._source.fetch_by_credentials(additional_node)
                Fetch.fetch_image(additional_node, img_path)
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
                        'image': str(img_path/f'{additional_node.id}.png'),
                        'shape': 'plaintext',
                        'labelloc': 'b',
                        'fixedsize': 'true',
                        'width': '1',
                        'height': '1',
                        'imagescale': 'true',
                        'fontsize': '8',
                    }
                )
                graph.edge(node.id, additional_node.id, _attributes={'color': additional_branch_color})
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
                'image': str(img_path / f'{node.id}.png'),
                'shape': 'plaintext',
                'labelloc': 'b',
                'fixedsize': 'true',
                'width': '1',
                'height': '1',
                'imagescale': 'true',
                'fontsize': '8',
            }
        )

        if previous_node is not None:
            graph.edge(previous_node.id, node.id, _attributes={'color': main_branch_color})
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
        'fontsize': '8'
    })

    graph.render(graph_name, graph_path, cleanup=True)
