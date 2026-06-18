from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app

client = TestClient(app)


def test_root_endpoint():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "LogSleuth"


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@patch("app.api.routes.logs.process_log.delay")
def test_create_log(mock_delay):

    payload = {
        "message": "database timeout",
        "level": "ERROR"
    }

    response = client.post(
        "/logs",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["status"] == "queued"


@patch("app.api.routes.logs.process_log.delay")
def test_create_log_with_metadata(mock_delay):

    payload = {
        "message": "database timeout",
        "level": "ERROR",
        "service": "auth-service",
        "host": "server-01",
        "metadata": {
            "environment": "production",
            "region": "ap-south-1"
        }
    }

    response = client.post(
        "/logs",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert data["status"] == "queued"


def test_get_logs():

    response = client.get("/logs")

    assert response.status_code == 200


def test_stats_endpoint():

    response = client.get("/logs/stats")

    assert response.status_code == 200

    data = response.json()

    assert "total_logs" in data
    assert "error_logs" in data
    assert "processed_logs" in data
