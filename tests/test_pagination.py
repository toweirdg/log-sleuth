from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_limit_parameter():

    response = client.get("/logs?limit=5")

    assert response.status_code == 200


def test_skip_parameter():

    response = client.get("/logs?skip=1")

    assert response.status_code == 200


def test_sort_parameter():

    response = client.get("/logs?sort_by=id")

    assert response.status_code == 200
