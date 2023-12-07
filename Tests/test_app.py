# tests/test_app.py
import json
import pytest
from app import app, save_tweets

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_create_tweet_success(client):
    """Test creating a new tweet with a successful request."""
    data = {
        "user_name": "John Doe",
        "text": "Test tweet",
        "hashtags": "pytest"
    }

    response = client.post('/tweets', json=data)
    assert response.status_code == 201  # Created
    assert response.json['user_name'] == data['user_name']
    assert response.json['text'] == data['text']

def test_create_tweet_failure(client):
    """Test creating a new tweet with an unsuccessful request."""
    data = {
        "user_name": "John Doe",  # Missing 'text' field
        "hashtags": "pytest"
    }

    response = client.post('/tweets', json=data)
    assert response.status_code == 400  # Bad Request
    assert "Bad or incomplete request" in response.get_data(as_text=True)

def test_get_all_tweets_success(client):
    """Test getting all tweets with a successful request."""
    response = client.get('/tweets')
    assert response.status_code == 200  # OK
    assert isinstance(response.json, list)

def test_get_all_tweets_failure(client):
    """Test getting all tweets with an unsuccessful request."""
    # Assuming there's no change in the implementation for this test
    response = client.get('/tweets_invalid')
    assert response.status_code == 404  # Not Found
    assert "Not Found" in response.get_data(as_text=True)


