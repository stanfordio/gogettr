from lib import PublicClient

client = PublicClient()


def test_all_posts():
    """Verifies we can extract the first five posts."""
    posts = list(client.all_posts(max=5))
    assert len(posts) == 5


def test_user_posts_downward():
    """Verifies that we can pull posts backward."""
    posts = list(client.all_posts(last="pew9", max=10, order="down"))
    assert len(posts) == 10


def test_user_posts_limited_id():
    """Verifies that we can pull posts backward with an ID as the endpoint."""
    posts = list(client.all_posts(last="pew9", first="pew0", order="down"))
    assert len(posts) > 0
