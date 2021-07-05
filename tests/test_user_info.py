from lib.errors import GettrApiError
from lib import PublicClient

client = PublicClient()


def test_user_info():
    """Verifies we can extract user info for a simple, known user."""
    resp = client.user_info(username="support")
    assert resp["nickname"] == "support"
    assert resp["username"] == "support"
    assert resp["ousername"] == "support"
    assert resp["roles"]["infl"]["lvl"] == 5


def test_user_info_nonexistent():
    """Verifies that we safely can pull the user info of a nonexistent user."""
    try:
        client.user_info(username="fsjdhflqkdsjfhlaskfjdhlaksdhluweh") # If someone registers this name, just change the test
        assert False # This should error
    except GettrApiError as e:
        assert e.args[0]["code"] == "E_USER_NOTFOUND"
