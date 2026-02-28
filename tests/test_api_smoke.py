from fastapi.testclient import TestClient

from src.api import app


def test_health():
    c = TestClient(app)
    r = c.get('/health')
    assert r.status_code == 200
    assert r.json().get('ok') is True


def test_summarize_validation():
    c = TestClient(app)
    r = c.post('/summarize', json={'text': '   '})
    assert r.status_code == 422
