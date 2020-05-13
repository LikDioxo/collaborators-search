import scholarly as sc
from collections import defaultdict


def bfs(start, goal):
    queue = [start]
    level = defaultdict(lambda: None)
    level[start.id] = (0, [start])
    while queue:
        v = queue.pop(0)
        v.fill()
        print(v.name)
        for w in v.coauthors:

            print(w.name)
            if level[w.id] is None:
                level[w.id] = (level[v.id][0] + 1, level[v.id][1] + [w])
                queue.append(w)

                if w.id == goal.id:
                    w.fill()
                    return level[w.id]

    return None, None


test = sc.search_author("Андрій Стрюк")
goal = sc.search_author("Кузнєцов Денис Іванович")
t = next(test)
g = next(goal)
print(t)
levl, path = bfs(t, g)

print(f"Level:{levl}")
print("->".join([e.name for e in path]))




