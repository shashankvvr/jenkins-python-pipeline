from app import lookup_status

def test_lookup_status():
    assert lookup_status() == "System Operational"