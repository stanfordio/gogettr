"""Tests for the 'registration_status' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_registration_status_found():
    assert client.is_registered("dineshdsouza").get("registered")


def test_registration_status_not_found():
    assert not client.is_registered("fekewgkfgewkhfgewkhfg").get("registered")
