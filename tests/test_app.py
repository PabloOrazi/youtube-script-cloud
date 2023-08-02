import json
import base64
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    # Test the index route
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!doctype html>" in response.data

def test_post_request(client):
    # Test the '/return_transcript' POST route
    input_data = {
        "inputYouTubeUrl": "https://www.youtube.com/watch?v=OJDkPz3nPjM"
    }

    response = client.post("/return_transcript", data=json.dumps(input_data), content_type="application/json")
    assert response.status_code == 200

    data = response.get_json()
    assert "image" in data
    assert "video_title" in data
    assert "url" in data
    assert "url_youtube" in data

    # Check that the image data is encoded as base64
    assert isinstance(data["image"], str)
    assert base64.b64decode(data["image"], validate=True)

