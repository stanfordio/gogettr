"""Tests for the 'user-info' capability."""

from gogettr import PublicClient
from gogettr.errors import GettrApiError

client = PublicClient()


def test_user_info():
    """Verifies we can extract user info for a simple, known user."""
    resp = client.user_info(username="support")
    print(resp)
    assert resp["nickname"] == "Support & Help"
    assert resp["username"] == "support"
    assert resp["ousername"] == "support"
    assert resp["infl"] == 5


def test_user_info_nonexistent():
    """Verifies that we safely can pull the user info of a nonexistent user."""
    try:
        client.user_info(
            username="fsjdhflqkdsjfhlaskfjdhlaksdhluweh"
        )  # If someone registers this name, just change the test
        assert False  # This should error
    except GettrApiError as err:
        assert err.issue["code"] == "E_USER_NOTFOUND"
