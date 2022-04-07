from fastapi.testclient import TestClient

from app.main import app

from .utils import generate_code

client = TestClient(app)
url = "https://fondeadora.com/"


def test_generate_code():
    """Test generate a user friendly code"""
    code = generate_code()
    assert isinstance(code, str)
    assert len(code) == 4


def test_create_shortcode_url():
    """Test endpoint to generate a shortcode"""
    payload = {"url": url}
    response = client.post("/", json=payload)
    shortener = response.json()
    assert response.status_code == 201
    assert "url" in shortener
    assert "code" in shortener


def test_create_shortcode_url_wrong_format():
    """Test endpoint to generate a shortcode with url in bad format"""
    url = "string"
    response = client.post("/", json={"url": url})
    data = response.json()
    assert response.status_code == 422
    assert "detail" in data
    assert "msg" in data["detail"][0]
    assert data["detail"][0]["msg"] == "invalid or missing URL scheme"
