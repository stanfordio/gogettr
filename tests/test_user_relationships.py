"""Tests for the 'user_relationships' (following/followers) capability."""

from gogettr import PublicClient

client = PublicClient()


def test_user_following():
    """Verifies we can extract who a user is following."""
    resp = list(
        client.user_relationships(username="etaoinshrdlu", type="following", max=50)
    )
    assert "JasonMillerinDC" in [user["ousername"] for user in resp]


def test_user_followers():
    """Verifies we can extract a user's followers."""
    resp = list(
        client.user_relationships(username="dineshdsouza", type="followers", max=501)
    )
    assert len(resp) == 501
