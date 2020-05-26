from coauthors_search.structures import AuthorCredentials


class Source:

    def fetch_by_name(self, name: str):
        ...

    def fetch_by_credentials(self, credentials: AuthorCredentials):
        ...
