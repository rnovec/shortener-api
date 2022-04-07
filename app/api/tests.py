from fastapi.testclient import TestClient

from app.main import app

from .utils import generate_code

client = TestClient(app)
url = "https://fondeadora.com/"


def test_generate_code():
    code = generate_code()
    assert isinstance(code, str)
    assert len(code) == 4

