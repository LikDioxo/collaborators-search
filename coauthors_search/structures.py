from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass
class AuthorCredentials:
    id: str
    name: str
    _source: str


@dataclass
class Author:
    id: str
    name: str
    affiliation: str
    coauthors: List[AuthorCredentials]
    url_picture: str
    _source: str
    picture_path: Path = None

    def get_short_name(self, quantity=25):
        return self.name[:quantity] + "..."

    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False


@dataclass
class Tree:
    tree: Dict[str, List[Author]] = None

    def create_tree(self, root: Author, goal: Author):
        queue = [root]
        level = defaultdict(lambda: None)
        level[root.id] = [root]
        while queue:
            v = queue.pop(0)
            for w in v.coauthors:
                w = w._source.fetch_by_credentials(w)
                if level[w.id] is None:
                    level[w.id] = level[v.id] + [w]
                    queue.append(w)

                    if w.id == goal.id:
                        self.tree = level
                        return level[w.id]
