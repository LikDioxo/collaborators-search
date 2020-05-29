from multiprocessing import Pool, freeze_support

from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch, create_dirs
from coauthors_search.structures import Tree
from coauthors_search.images import generate_graph2

if __name__ == '__main__':
    parent_path = r"C:\Users\User\Pythonprojects\collaborators-search"
    dir_name = "test"
    graph_dir_name = "test_graph"
    test = Fetch(ScholarSource())
    a = test.fetch_author_by_name('Андрій Стрюк')[0]
    b = test.fetch_author_by_name('Наталя Рашевська')[0]
    my_tree = Tree()
    my_tree.create_tree(a, b)
    my_configuration = {
        'graph_type': 'directed',
        'additional_nodes': 2,
        'main_branch_color': 'red',
        'additional_branch_color': 'blue',
        'graph_path': r"C:\Users\User\Pythonprojects\collaborators-search\test\test_graph\\",
        'image_path': r"C:\Users\User\Pythonprojects\collaborators-search\test\images\\",
        'graph_name': "test_graph_name"
    }
    create_dirs(parent_path, dir_name, graph_dir_name)
    generate_graph2(my_tree, b, configuration=my_configuration)
