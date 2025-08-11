import sys
import os
import json

# Make sure the parent directory (root of repo) is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_addition():
    assert 1 + 1 == 2

def test_home_route():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
