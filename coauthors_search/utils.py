from requests import get
from shutil import copyfileobj

from coauthors_search.sources import Source
from coauthors_search.structures import AuthorCredentials, Author


class Fetch:
    def __init__(self, source: Source):
        self.source = source

    def fetch_author_by_name(self, name: str):
        return self.source.fetch_by_name(name)

    def fetch_author_by_credentials(self, credentials: AuthorCredentials):
        return self.source.fetch_by_credentials(credentials)

    def fetch_image(self, author: Author):
        file_path = f'images/{author.id}.png'
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
