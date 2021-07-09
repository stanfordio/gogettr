"""Tests for the 'comments' (from post) capability."""

from gogettr import PublicClient

client = PublicClient()


def test_comments_from_post():
    """Verifies we can get comments from a post"""
    resp = list(client.comments(post_id="p2vhax", max=50))
    assert len(resp) == 50
