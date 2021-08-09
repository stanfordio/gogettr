"""Tests for the 'hashtag' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_suggested_hashtags():
    """Verifies we can extract suggested hashtags."""
    resp = list(client.hashtags(max=10))
    assert len(resp) == 5  # max seems to be 5 now

    # Later results (e.g., past #5) won't have expanded info
    assert "hashtag" in resp[0]
    assert ("description" in resp[0]) or ("score" in resp[0])
