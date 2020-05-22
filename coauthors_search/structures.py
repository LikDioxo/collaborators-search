from dataclasses import dataclass
from typing import Dict, List


@dataclass
class AuthorCredentials:
    name: str


@dataclass
class Author:
    id: str
    name: str
    affiliation: str
    contributors: List[AuthorCredentials]


@dataclass
class Tree:
    tree: Dict[str, List[Author]]
