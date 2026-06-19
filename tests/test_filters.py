from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_filter_by_level():

    response = client.get("/logs?level=ERROR")

    assert response.status_code == 200


def test_filter_by_status():

    response = client.get("/logs?status=processed")

    assert response.status_code == 200


def test_filter_by_severity():

    response = client.get("/logs?severity=CRITICAL")

    assert response.status_code == 200
