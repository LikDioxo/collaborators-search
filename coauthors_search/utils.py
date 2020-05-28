from multiprocessing import Pool
from os import makedirs, path
from requests import get
from shutil import copyfileobj
from typing import List

from coauthors_search.sources import Source
from coauthors_search.structures import AuthorCredentials, Author


class Fetch:
    def __init__(self, source: Source):
        self.source = source

    def fetch_author_by_name(self, name: str):
        return self.source.fetch_by_name(name)

    def fetch_author_by_credentials(self, credentials: AuthorCredentials):
        return self.source.fetch_by_credentials(credentials)

    def fetch_multiple_authors(self, names: List[str], pool: Pool):
        return pool.map(self.fetch_author_by_name, names)

    @staticmethod
    def fetch_image(author: Author, file_path: str):
        file_path = path.join(file_path, f'{author.id}.png')
        author.picture_path = file_path
        with open(file_path, 'wb') as file:
            try:
                resp = get(author.url_picture, stream=True)
            except AttributeError:
                ...
            else:
                resp.raw.decode_content = True
                copyfileobj(resp.raw, file)
                del resp


def create_dirs(parent_path: str, dir_name: str, graph_dir_name: str):
    parent_path = path.join(parent_path, dir_name)
    image_path = path.join(parent_path, "images")
    graph_path = path.join(parent_path, graph_dir_name)
    try:
        makedirs(parent_path)
    except OSError:
        ...

    try:
        makedirs(image_path)
    except OSError:
        ...

    try:
        makedirs(graph_path)
    except OSError:
        ...


def validate_configuration(requirements, default_configs):
    def decorator(func):
        def wrapper(*args, configuration=None):

            if configuration is None:
                raise ValueError("Missing configuration parameter!")

            for r in requirements:
                if r not in configuration.keys():
                    raise ValueError(f"Missing requirement configuration: '{r}'")

            for key in default_configs.keys():
                if key not in configuration.keys():
                    configuration[key] = default_configs[key]

            return func(*args, configuration=configuration)

        return wrapper

    return decorator
