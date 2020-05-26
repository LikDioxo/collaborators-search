from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch
from coauthors_search.structures import Tree
from coauthors_search.images import generate_graph


if __name__ == '__main__':
    test = Fetch(ScholarSource())
    a = next(test.fetch_author_by_name('Андрій Стрюк'))
    b = next(test.fetch_author_by_name('Наталя Рашевська'))
    my_tree = Tree()
    my_tree.create_tree(a, b)
    my_configuration = {
        'graph_type': 'directed',
        'format': 'png',
        'additional_nodes': 2
    }

    generate_graph(my_tree, b, my_configuration)
