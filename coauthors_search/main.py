from multiprocessing import Pool, freeze_support
from pathlib import Path

from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch, create_dirs
from coauthors_search.structures import Tree
from coauthors_search.images import generate_graph2

ROOT_DIR = Path(__file__).parent
DIR_PATH = ROOT_DIR / "default"
GRAPH_DIR_PATH = DIR_PATH / "default_graph"

if __name__ == '__main__':
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
        'graph_path': GRAPH_DIR_PATH,
        'image_path': DIR_PATH / 'images',
        'graph_name': "test_graph_name"
    }
    create_dirs(DIR_PATH, GRAPH_DIR_PATH)
    generate_graph2(my_tree, b, configuration=my_configuration)
