from lib.capabilities import user_posts, all_posts
from lib.api import ApiClient


class PublicClient:
    """A client for all the public GETTR methods. If it doesn't require an account, it belongs here."""

    def __init__(self):
        self.api_client = ApiClient()

        # Fill this class
        self._user_posts = user_posts.UserPosts(self.api_client)
        self._all_posts = all_posts.AllPosts(self.api_client)

    def user_posts(self, *args, **kwargs):
        """Pull the users' posts from the API."""
        # TODO: document parameters

        return self._user_posts.pull(*args, **kwargs)

    def all_posts(self, *args, **kwargs):
        """Pulls all the posts from the API."""
        # TODO: document parameters
        return self._all_posts.pull(*args, **kwargs)
