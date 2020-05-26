from typing import Dict, Any

from graphviz import Graph, Digraph

from coauthors_search.structures import Tree
from coauthors_search.structures import Author


def generate_graph(tree: Tree, target: Author, configuration: Dict[str, Any]):
    graph = None

    if configuration['graph_type'] == 'directed':
        graph = Digraph()
    else:
        graph = Graph()

    # if configuration['layout'] == 'horizontal':
    #     graph.engine = 'neato'

    graph.name = "Authors"
    graph.format = configuration['format']

    main_branch = tree.tree[target.id]
    additional_nodes_limit = configuration['additional_nodes']

    previous_node = None
    nodes = []
    for node in main_branch:
        test(node)
        additional_nodes = 0
        nodes.append(node.id)

        for additional_node in tree.tree[node.id]: #TODO: tree.tree[node.id] is a path not childs! fix
            if additional_node.id not in nodes and additional_nodes <= additional_nodes_limit:
                print(additional_node)
                test(additional_node)
                additional_nodes += 1
                graph.node(
                    str(additional_node.id),
                    '',
                    {
                        'label': f"""<<TABLE border="0">
                        <TR>
                            <TD  bgcolor="white" border="0">{additional_node.name}</TD>
                        </TR>
                        </TABLE>>""",
                        'image': f'images/{additional_node.id}.png',
                        'shape': 'plaintext',
                        'labelloc': 'b',
                        'fixedsize': 'true',
                        'width': '1',
                        'height': '1',
                        'imagescale': 'true',
                        'fontsize': '10'
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
                    <TD  bgcolor="white" border="0">{node.name}</TD>
                </TR>
                </TABLE>>""",
                'image': f'images/{node.id}.png',
                'shape': 'plaintext',
                'labelloc': 'b',
                'fixedsize': 'true',
                'width': '1',
                'height': '1',
                'imagescale': 'true',
                'fontsize': '10'
            }
        )

        if previous_node is not None:
            graph.edge(previous_node.id, node.id)
        previous_node = node

    graph.view()


def test(author: Author):
    from coauthors_search.utils import Fetch
    from coauthors_search.sources import Source
    f = Fetch(Source())
    f.fetch_image(author)
