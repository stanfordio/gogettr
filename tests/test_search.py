from gogettr import PublicClient

client = PublicClient()


def test_basic_search():
    """Verifies we can perform a basic search."""
    posts = list(client.search(query="America", max=1776))
    assert len(posts) == 1776

    for post in posts:
        assert "america" in post["txt"].lower()

        # Check whether user info is present
        assert "ousername" in post["uinf"]


def test_paginated_search():
    """Verifies we can perform a paginated search."""
    posts = list(client.search(query="x", max=5000))
    assert len(posts) == 5000
