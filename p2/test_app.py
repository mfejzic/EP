import requests
import os

BASE_URL = "http://localhost:5000"


def test_home():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert "message" in r.json()


def test_env():
    r = requests.get(f"{BASE_URL}/env")
    assert r.status_code == 200