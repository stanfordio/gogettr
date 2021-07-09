"""Tests for the 'comments' (from post) capability."""

from gogettr import PublicClient

client = PublicClient()


POST_NO_COMMENTS = "p2zkgu"
POST_TWO_COMMENTS = "p2zp65"


def test_comments_from_post():
    """Verifies we can get comments from a post."""
    resp = list(client.comments(post_id="p2vhax", max=50))
    assert len(resp) == 50


def test_comments_from_post_no_comments():
    """Verifies we can get comments from a post with no comments."""
    resp = list(client.comments(post_id=POST_NO_COMMENTS, max=3))
    assert len(resp) == 0


def test_comments_from_post_two_comments():
    """Verifies we can get comments from a post with only two comments."""
    resp = list(client.comments(post_id=POST_TWO_COMMENTS, max=3))
    assert len(resp) == 2
