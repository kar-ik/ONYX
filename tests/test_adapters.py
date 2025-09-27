import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from onyx.adapters.google import GoogleAdapter
from onyx.adapters.hibp import HIBPAdapter

def test_google_adapter():
    with pytest.raises(ValueError):  
        adapter = GoogleAdapter("dummy_key", "dummy_cx")
    adapter = HIBPAdapter()
    assert adapter.healthcheck()['status'] == "healthy"

def test_hibp_adapter():
    adapter = HIBPAdapter()
    assert adapter.name == "hibp"
    assert adapter.healthcheck()['status'] == "healthy"
