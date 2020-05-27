from scholarly import scholarly

from coauthors_search.sources import Source
from coauthors_search.structures import Author, AuthorCredentials


class ScholarSource(Source):

    def fetch_by_name(self, name: str):
        res = []
        for author in scholarly.search_author(name):
            author.fill(['coauthors'])
            coauthors = []
            for e in author.coauthors:
                e.fill(['basics'])
                coauthors.append(AuthorCredentials(name=e.name, id=e.id, _source=ScholarSource()))

            res.append(Author(
                id=author.id,
                name=author.name,
                affiliation=author.affiliation,
                coauthors=coauthors,
                url_picture=author.url_picture,
                _source=ScholarSource()
            ))
        return res

    def fetch_by_credentials(self, credentials: AuthorCredentials):
        for author in scholarly.search_author(credentials.name):
            if author.id == credentials.id:
                author.fill(['coauthors'])
                coauthors = []
                for e in author.coauthors:
                    e.fill(['basics'])
                    coauthors.append(AuthorCredentials(name=e.name, id=e.id, _source=ScholarSource()))

                return Author(
                    id=author.id,
                    name=author.name,
                    affiliation=author.affiliation,
                    coauthors=coauthors,
                    url_picture=author.url_picture,
                    _source=ScholarSource()
                )
