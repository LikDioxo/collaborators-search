from bfs import Collaboration
from scholarly import search_author


if __name__ == '__main__':
    test = Collaboration(
        first_author=next(search_author("Андрій Стрюк")),
        second_author=next(search_author("Рашевська Наталя")),
        level=None,
        collaboration_path=None
    )
    test.bfs()
    print(test.level)
    print(test.collaboration_path)
