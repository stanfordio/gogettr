"""Tests for the 'registration_status' capability."""

from gogettr import PublicClient

client = PublicClient()


def test_registration_status_found():
    assert client.is_registered("dineshdsouza")
    
def test_registration_status_found():
    assert not client.is_registered("fekewgkfgewkhfgewkhfg")