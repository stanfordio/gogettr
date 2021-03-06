"""Tests for the 'all' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_all_posts():
    """Verifies we can extract the first five posts."""
    posts = list(client.all(max=5))
    assert len(posts) == 5


def test_user_posts_downward():
    """Verifies that we can pull posts backward."""
    posts = list(client.all(last="pew9", max=10, order="down"))
    assert len(posts) == 10


def test_user_posts_limited_id():
    """Verifies that we can pull posts backward with an ID as the endpoint."""
    posts = list(client.all(last="pew9", first="pew0", order="down"))
    assert len(posts) > 0


def test_all_comments():
    """Verifies we can extract the first five comments."""
    comments = list(client.all(max=5, type="comments"))
    assert len(comments) == 5
