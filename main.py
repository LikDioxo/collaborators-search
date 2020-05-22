from coauthors_search.integration.scholar import ScholarSource
from coauthors_search.utils import Fetch

if __name__ == '__main__':
    test = Fetch(ScholarSource())
    a = test.fetch_author('Андрій Стрюк')
    for e in a:
        print(e)
