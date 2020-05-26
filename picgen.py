from requests import get
from shutil import copyfileobj

from graphviz import Digraph

from coauthors_search.structures import Tree, Author


def generate_image(tree: Tree):
    graph = Digraph('Collaboration', format="png")
    my_nodes = []
    for k in tree.tree:
        for e in tree.tree[k]:
            get_image(e)
            graph.node(
                str(e.id),
                '',
                {
                    'label': f"""<<TABLE border="0">
                            <TR>
                                <TD  bgcolor="white" border="0">{e.name}</TD>
                            </TR>
                            </TABLE>>""",
                    'image': f'images/{e.id}.png',
                    'shape': 'plaintext',
                    'labelloc': 'b',
                    'fixedsize': 'true',
                    'width': '1',
                    'height': '1',
                    'imagescale': 'true',
                    'fontsize': '10'
                }
            )
            my_nodes.append(str(e.id))

    for i in range(len(my_nodes) - 1):
        graph.edge(my_nodes[i], my_nodes[i + 1])

    graph.view()

def get_image(author: Author):
    with open(f'images/{author.id}.png', 'wb') as file:
        try:
            resp = get(author.url_picture, stream=True)
        except AttributeError:
            ...
        else:
            resp.raw.decode_content = True
            copyfileobj(resp.raw, file)
            del resp