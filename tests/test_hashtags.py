from gogettr import PublicClient

client = PublicClient()


def test_suggested_hashtags():
    """Verifies we can extract suggested hashtags."""
    resp = list(client.hashtags(max=50))
    assert len(resp) == 50

    # Later results (e.g., past #5) won't have expanded info
    assert "hashtag" in resp[0]
    assert "description" in resp[0]
