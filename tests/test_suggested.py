from gogettr import PublicClient

client = PublicClient()


def test_suggested():
    """Verifies we can extract suggested users."""
    resp = list(client.suggested(max=50))
    assert len(resp) == 50
    assert "nickname" in resp[0]  # Verify that it is actual user data
    assert "dsc" in resp[0]
