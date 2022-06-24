"""Tests for the 'trends' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_trends():
    """Verifies we can extract trending posts."""
    # resp = list(client.trends(max=5))
    # assert len(resp) > 0
    # TODO(milesmcc): reactivate this test when GETTR puts posts back on its homepage
