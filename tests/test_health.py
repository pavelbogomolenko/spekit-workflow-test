import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


# User Story 1: Operators Check Application Status


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_json_status_ok(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}


def test_health_content_type_is_json(client):
    response = client.get("/health")
    assert response.content_type == "application/json"


# User Story 2: Automated Deployment Validation


def test_health_no_auth_required(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_post_returns_405(client):
    response = client.post("/health")
    assert response.status_code == 405


def test_health_delete_returns_405(client):
    response = client.delete("/health")
    assert response.status_code == 405
