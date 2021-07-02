from lib import PublicClient

client = PublicClient()


def test_user_posts():
    """Verifies we can extract posts for a simple, known user."""
    posts = list(client.user_posts(username="support", max=5))
    assert len(posts) > 0


def test_user_posts_max():
    """Verifies that we pull at most `max` posts."""
    posts = list(client.user_posts(username="dailynews", max=10))
    assert len(posts) == 10
