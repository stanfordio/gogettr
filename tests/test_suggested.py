"""Tests for the 'suggested' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_suggested():
    """Verifies we can extract suggested users."""
    resp = list(client.suggested(max=50))
    assert len(resp) == 50
    # Verify the response shape (rather than optional per-user fields like
    # `dsc`, which not every suggested account has).
    assert resp[0].get("_t") == "uinf"
    assert "username" in resp[0]
