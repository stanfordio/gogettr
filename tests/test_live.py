"""Tests for the 'live' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_live_all():
    """Gets 50 livestreams"""
    resp = list(client.live(max=50))
    assert len(resp) == 50
