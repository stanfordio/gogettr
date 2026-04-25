"""Tests for the 'search' capability."""

import pytest

from gogettr import PublicClient

client = PublicClient()

# GETTR's /u/posts/srch/phrase endpoint currently returns HTTP 500 for every
# query (E_API_ERROR). When the upstream service recovers these will start
# passing again; until then xfail keeps the suite green without hiding the gap.
SEARCH_BROKEN = pytest.mark.xfail(
    reason="GETTR /u/posts/srch/phrase returns HTTP 500 for all queries",
    strict=False,
)


@SEARCH_BROKEN
def test_basic_search():
    """Verifies we can perform a basic search."""
    posts = list(client.search(query="stanford", max=200))
    assert len(posts) > 50  # GETTR's number of search results is inconsistent

    for post in posts:
        assert "stanford" in post["txt"].lower()

        # Check whether user info is present
        assert "ousername" in post["uinf"]


@SEARCH_BROKEN
def test_paginated_search():
    """Verifies we can perform a paginated search."""
    posts = list(client.search(query="x", max=500))
    assert len(posts) > 50  # GETTR's number of search results is inconsistent
