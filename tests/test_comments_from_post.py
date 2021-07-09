"""Tests for the 'comments' (from post) capability."""

from gogettr import PublicClient

client = PublicClient()


post_no_comments= "p2zkgu"
post_two_comments="p2zp65"

def test_comments_from_post():
    """Verifies we can get comments from a post"""
    resp = list(client.comments(post_id="p2vhax", max=50))
    assert len(resp) == 50
    
    
def test_comments_from_post_no_comments():
    """Verifies we can get comments from a post"""
    resp = list(client.comments(post_id=post_no_comments, max=3))
    assert len(resp) == 0
    
def test_comments_from_post_two_comments():
    """Verifies we can get comments from a post"""
    resp = list(client.comments(post_id=post_two_comments, max=3))
    assert len(resp) == 2
    
