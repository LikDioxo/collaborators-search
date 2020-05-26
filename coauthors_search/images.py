from typing import Dict

from graphviz import Graph, Digraph

from coauthors_search.structures import Tree
from coauthors_search.structures import Author


def generate_graph(tree: Tree, target: Author, configuration: Dict[str, str]):
    graph = None

    if configuration['graph_type'] == 'directed':
        graph = Digraph()
    else:
        graph = Graph()

    if graph is None:
        raise ValueError('missing requirement ')

    if configuration['layout'] == 'horizontal':
        graph.engine = 'neato'

    graph.name = "Authors"
    graph.format = configuration['format']

