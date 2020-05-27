from multiprocessing import Pool, freeze_support

from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch
from coauthors_search.structures import Tree
from coauthors_search.images import generate_graph


if __name__ == '__main__':
    freeze_support()
    pool = Pool(5)
    test = Fetch(ScholarSource())
    test_m = test.fetch_multiple_authors(["Стрюк","Рашевська","Рассовицька", "Кислова", "Шаповалова"], pool)
    for au in test_m:
        for e in au:
            print(e.name+"\n___________")
        print("___________________")
    # a = next(test.fetch_author_by_name('Андрій Стрюк'))
    # b = next(test.fetch_author_by_name('Наталя Рашевська'))
    # my_tree = Tree()
    # my_tree.create_tree(a, b)
    # # my_configuration = {
    # #     'graph_type': 'directed',
    # #     'format': 'png',
    # #     'additional_nodes': 2
    # # }
    # print(my_tree.tree)
    # generate_graph(my_tree, b, my_configuration)
