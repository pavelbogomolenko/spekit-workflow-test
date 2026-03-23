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


# T003: Nav-bar invariant tests — must fail before base.html is wired up
def test_root_has_main_navigation(client):
    response = client.get("/")
    assert b'<nav aria-label="Main navigation">' in response.data


def test_about_has_main_navigation(client):
    response = client.get("/about")
    assert b'<nav aria-label="Main navigation">' in response.data


def test_404_has_main_navigation(client):
    response = client.get("/does-not-exist")
    assert b'<nav aria-label="Main navigation">' in response.data


# T004: US1 — GET / returns 200 with Home aria-current and link to /about
def test_root_has_home_aria_current(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'aria-current="page"' in response.data


def test_root_has_link_to_about(client):
    response = client.get("/")
    assert b'href="/about"' in response.data


# T005: US1 — GET /about returns 200 with About aria-current and link to /
def test_about_returns_200(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_about_has_about_aria_current(client):
    response = client.get("/about")
    assert b'aria-current="page"' in response.data


def test_about_has_link_to_home(client):
    response = client.get("/about")
    assert b'href="/"' in response.data


# T009: US2 — GET /does-not-exist returns 404 with nav and no Traceback
def test_404_returns_404_status(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404


def test_404_no_traceback(client):
    response = client.get("/does-not-exist")
    assert b"Traceback" not in response.data
