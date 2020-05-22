from scholarly import Author, search_author

from coauthors_search.sources import Source
from coauthors_search.structures import Author, AuthorCredentials


class ScholarSource(Source):

    def fetch(self, credentials: str):
        for author in search_author(credentials):
            author.fill()
            contributors = [
                AuthorCredentials(name=e.name)
                for e in author.coauthors
            ]
            yield Author(
                id=author.id,
                name=author.name,
                affiliation=author.affiliation,
                contributors=contributors
            )
