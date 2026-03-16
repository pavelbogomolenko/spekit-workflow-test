def test_get_root_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_root_contains_greeting(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data


def test_unknown_path_returns_404(client):
    response = client.get("/unknown")
    assert response.status_code == 404


def test_unknown_path_body_is_human_readable(client):
    response = client.get("/unknown")
    assert len(response.data) > 0
    assert b"Traceback" not in response.data
