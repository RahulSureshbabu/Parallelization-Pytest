import requests

BASE = "http://localhost:3000"

def test_get_hello_status():
    r = requests.get(f"{BASE}/hello")
    assert r.status_code == 200

def test_get_hello_json():
    r = requests.get(f"{BASE}/hello")
    assert r.headers["Content-Type"].startswith("application/json")

def test_get_hello_message_field():
    r = requests.get(f"{BASE}/hello")
    data = r.json()
    assert "message" in data

def test_get_hello_value():
    r = requests.get(f"{BASE}/hello")
    data = r.json()
    assert data["message"] == "Hello World!"

def test_put_hello_status():
    r = requests.put(f"{BASE}/hello", json={"message": "Test PUT"})
    assert r.status_code == 200

def test_put_hello_updates_message():
    msg = "Updated via test"
    r = requests.put(f"{BASE}/hello", json={"message": msg})
    assert r.json()["updated"] == msg

def test_put_missing_message():
    r = requests.put(f"{BASE}/hello", json={})
    # This SHOULD be 400, but your API returns 200.
    # Update your API to fix this.
    assert r.status_code == 400

