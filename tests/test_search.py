"""Tests for the 'search' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_basic_search():
    """Verifies we can perform a basic search."""
    posts = list(client.search(query="stanford", max=200))
    assert len(posts) > 50  # GETTR's number of search results is inconsistent

    for post in posts:
        assert "stanford" in post["txt"].lower()

        # Check whether user info is present
        assert "ousername" in post["uinf"]


def test_paginated_search():
    """Verifies we can perform a paginated search."""
    posts = list(client.search(query="x", max=500))
    assert len(posts) > 50  # GETTR's number of search results is inconsistent
