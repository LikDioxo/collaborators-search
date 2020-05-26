from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch
from coauthors_search.structures import Tree
from picgen import generate_image


if __name__ == '__main__':
    test = Fetch(ScholarSource())
    a = test.fetch_author_by_name('Андрій Стрюк').__next__()
    b = test.fetch_author_by_name('Наталя Рашевська').__next__()
    my_tree = Tree()
    my_tree.create_tree(a, b)
    generate_image(my_tree)
