from multiprocessing import Pool, freeze_support

from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch
from coauthors_search.structures import Tree
from coauthors_search.images import generate_graph

if __name__ == '__main__':
    test = Fetch(ScholarSource())
    a = test.fetch_author_by_name('Андрій Стрюк')[0]
    b = test.fetch_author_by_name('Наталя Рашевська')[0]
    my_tree = Tree()
    my_tree.create_tree(a, b)
    my_configuration = {
        'graph_type': 'directed',
        'format': 'pdf',
        'additional_nodes': 2,
        'main_branch_color': 'red',
        'additional_branch_color': 'blue'
    }
    generate_graph(my_tree, b, my_configuration)
