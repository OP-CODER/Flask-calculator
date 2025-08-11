import json

def test_addition():
    assert 1 + 1 == 2

# Example Flask API test
def test_home_route():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
