# HTTP API Contracts: Python Hello World Web App

**Branch**: `002-python-hello-webapp` | **Date**: 2026-03-16

## Overview

This document defines the HTTP interface contracts for the web application. The app exposes one functional endpoint and a catch-all 404 handler. Contract tests MUST be written for both (Constitution Principle II).

---

## Endpoint 1 — Greeting

### `GET /`

Returns the "Hello, World!" greeting page.

**Request**

| Field | Value |
|-------|-------|
| Method | `GET` |
| Path | `/` |
| Headers | None required |
| Body | None |

**Response — Success**

| Field | Value |
|-------|-------|
| Status | `200 OK` |
| Content-Type | `text/html; charset=utf-8` |
| Body | HTML/text content containing `"Hello, World!"` |

**Example**

```http
GET / HTTP/1.1
Host: localhost:5000

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

Hello, World!
```

**Contract Test Assertions**

```python
def test_get_root_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_root_contains_greeting(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data
```

---

## Endpoint 2 — Not Found (catch-all)

### `GET /<unknown_path>`

Returns a 404 Not Found response for any path not explicitly registered.

**Request**

| Field | Value |
|-------|-------|
| Method | `GET` (and all other methods on unregistered paths) |
| Path | Any path other than `/` |
| Headers | None required |
| Body | None |

**Response — Not Found**

| Field | Value |
|-------|-------|
| Status | `404 Not Found` |
| Content-Type | `text/html; charset=utf-8` |
| Body | Human-readable error text (e.g., `"Not Found"`) |

**Example**

```http
GET /unknown HTTP/1.1
Host: localhost:5000

HTTP/1.1 404 NOT FOUND
Content-Type: text/html; charset=utf-8

Not Found
```

**Contract Test Assertions**

```python
def test_unknown_path_returns_404(client):
    response = client.get("/unknown")
    assert response.status_code == 404

def test_unknown_path_body_is_human_readable(client):
    response = client.get("/unknown")
    assert len(response.data) > 0
    # No raw stack traces or internal identifiers (Constitution III)
    assert b"Traceback" not in response.data
```

---

## Notes

- All contract tests belong in `tests/test_app.py` and MUST be written before the implementation (TDD — Constitution Principle II).
- The Flask test client fixture (`client`) is provided via a pytest fixture in `tests/conftest.py` or at the top of `tests/test_app.py`.
- No authentication, versioning, or request body parsing is required at this scope.
