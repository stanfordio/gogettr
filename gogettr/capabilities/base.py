from gogettr.api import ApiClient


class Capability:
    """Provides base functionality for the individual capabilities."""

    def __init__(self, client: ApiClient):
        self.client = client

    def pull(self, *args, **kwargs):
        """Pull the desired data from GETTR."""
        raise NotImplementedError
