import pytest
from onyx.adapters.google import GoogleAdapter
from onyx.adapters.hibp import HIBPAdapter

def test_google_adapter():
    adapter = GoogleAdapter("dummy_key", "dummy_cx")
    assert adapter.name == "google"
    assert adapter.healthcheck()['status'] == "healthy"

def test_hibp_adapter():
    adapter = HIBPAdapter()
    assert adapter.name == "hibp"
    assert adapter.healthcheck()['status'] == "healthy"
