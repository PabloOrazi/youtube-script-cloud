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

def test_post_request_transcript(client):
    # Test the '/get_transcript' POST route
    input_data = {
        "inputYouTubeUrl": "https://www.youtube.com/watch?v=OJDkPz3nPjM"
    }

    response = client.post("/get_transcript", data=json.dumps(input_data), content_type="application/json")
    assert response.status_code == 200

    data = response.get_json()
    assert "url" in data
    assert "language" in data
    assert "text" in data

    # Check that the returned URL, language, and text match the input data
    assert data["url"] == input_data["inputYouTubeUrl"]

    # Replace 'your_module' with the actual name of the module containing the functions.
    from functions import extract_id, download_script

    video_id = extract_id(input_data["inputYouTubeUrl"])
    language, text = download_script(video_id)
    assert data["language"] == language
    assert data["text"] == text


def test_post_request_wordcloud(client):
    # Test the '/get_wordcloud' POST route
    input_data = {
        "inputYouTubeUrl": "https://www.youtube.com/watch?v=OJDkPz3nPjM"
    }

    response = client.post("/get_wordcloud", data=json.dumps(input_data), content_type="application/json")
    assert response.status_code == 200

    data = response.get_json()
    assert "image" in data
    assert "video_title" in data
    assert "url" in data
    assert "url_youtube" in data

    # Check that the image data is encoded as base64
    assert isinstance(data["image"], str)
    assert base64.b64decode(data["image"], validate=True)

