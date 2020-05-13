from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple, Union

from scholarly import Author


@dataclass
class Collaboration:
    first_author: Author
    second_author: Author
    level: Union[None, int]
    collaboration_path: Union[None, Tuple[Author]]

    def bfs(self):
        queue = [self.first_author]

        graph = defaultdict(lambda: None)
        graph[self.first_author.id] = {
            'level': 0,
            'path': [self.first_author]
        }

        while queue:
            current_author = queue.pop(0)
            current_author.fill()
            print(current_author.name)
            for coauthor in current_author.coauthors:

                print(coauthor.name)
                if graph[coauthor.id] is None:
                    graph[coauthor.id] = {
                        'level':graph[current_author.id]['level'] + 1,
                        'path': graph[current_author.id]['path'] + [coauthor]
                    }
                    queue.append(coauthor)

                    if coauthor.id == self.second_author.id:
                        coauthor.fill()
                        self.level = graph[coauthor.id]['level']
                        self.collaboration_path = graph[coauthor.id]['path']
                        return None

        self.level = None
        self.collaboration_path = None



# test = sc.search_author("Андрій Стрюк")
# goal = sc.search_author("Кузнєцов Денис Іванович")
# t = next(test)
# g = next(goal)
# print(t)
# levl, path = bfs(t, g)
#
# print(f"Level:{levl}")
# print("->".join([e.name for e in path]))




