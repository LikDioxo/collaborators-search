from coauthors_search.sources import Source
from coauthors_search.structures import Author


class Fetch:
    def __init__(self, source: Source):
        self.source = source

    def fetch_author(self, credentials: str):
        return self.source.fetch(credentials)
