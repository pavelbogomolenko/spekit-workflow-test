# Research: Python Hello World Web App

**Branch**: `002-python-hello-webapp` | **Date**: 2026-03-16

## Overview

Phase 0 research for a minimal Python "Hello, World!" web application with a README. All Technical Context fields were resolved from the spec and existing project conventions; this document records the reasoning and confirms there are no NEEDS CLARIFICATION items.

---

## Finding 1 — Web Framework Choice

**Decision**: Flask 2.x

**Rationale**: Flask is the canonical lightweight web framework for simple Python web apps in 2024–2026. A "Hello, World!" web app requires: a single route (`GET /`), a plain-text or HTML response, and a 404 handler for unknown paths. Flask satisfies all three in under 15 lines of code with zero configuration. Its built-in `app.test_client()` integrates directly with pytest, making TDD frictionless.

**Alternatives considered**:
- **FastAPI**: Excellent for APIs but introduces async complexity, Pydantic dependency, and OpenAPI generation — all unnecessary overhead for a single-route hello-world app.
- **Django**: Full-stack framework with ORM, migrations, admin, templates engine — extreme over-engineering for this scope.
- **http.server (stdlib)**: No external dependency, but has no routing abstraction, no test client, and requires manual HTTP response construction. Makes FR-007 (404 for unknown routes) verbose to implement correctly.
- **Bottle**: Similar to Flask but smaller ecosystem, less maintained, and fewer learning resources. No meaningful advantage over Flask here.

---

## Finding 2 — Response Format

**Decision**: Plain HTML with `"Hello, World!"` text in the body; `Content-Type: text/html`

**Rationale**: A web browser renders the response (US-001). Plain HTML — even just a bare text string — satisfies FR-001 and renders correctly in all browsers. A full HTML document template adds no user value at this scale. Flask's default `Content-Type` for string responses is `text/html; charset=utf-8`, which is correct.

**Alternatives considered**:
- Full HTML page (`<html><body><h1>Hello, World!</h1></body></html>`): Valid and slightly more "correct" HTML, but the spec does not require semantic markup — only that the message is displayed. Either form is acceptable; minimal string is simpler and easier to test exactly.
- JSON (`{"message": "Hello, World!"}`): Not a web page; does not satisfy the browser display requirement of US-001 without a frontend rendering layer.

---

## Finding 3 — 404 Handling

**Decision**: Flask's default `@app.errorhandler(404)` returning `"Not Found", 404`

**Rationale**: FR-007 requires undefined routes to return an appropriate error response. Flask automatically returns 404 for unregistered routes. A custom error handler is registered to ensure the response body is human-readable (Constitution Principle III) and testable via the test client.

**Alternatives considered**:
- Default Flask 404 (no custom handler): Returns Flask's HTML error page, which is acceptable but untestable for exact content. A custom handler gives deterministic test assertions.
- Returning 200 with an error message: Incorrect HTTP semantics; violates FR-007.

---

## Finding 4 — Port Configuration

**Decision**: Flask default port 5000; configurable via environment variable `PORT`

**Rationale**: The spec states "Default port configuration is acceptable; no specific port is mandated." Flask defaults to port 5000. Exposing a `PORT` environment variable allows developers to override without code changes — a best practice for local dev that adds minimal complexity. README documents the default (FR-005, FR-006).

**Alternatives considered**:
- Hard-coded port 8000: Common for Django/uvicorn convention; no advantage here.
- Hard-coded port 5000 only: Less flexible; the one-line `os.environ.get("PORT", 5000)` pattern is the idiomatic Flask approach.

---

## Finding 5 — Python Version Target

**Decision**: Python 3.8+ (consistent with existing project, feature 001)

**Rationale**: The project already targets Python 3.8+ (see 001-python-hello-world plan.md). Flask 2.x supports Python 3.8+. Maintaining version consistency avoids developer confusion and keeps prerequisites unified.

**Alternatives considered**:
- Python 3.10+ (match latest Flask recommendation): Flask 3.x requires Python 3.10+. Using Flask 2.x allows us to stay at the project's existing 3.8+ floor without sacrificing any needed features.

---

## Finding 6 — Testing Approach

**Decision**: pytest + Flask test client (`app.test_client()`)

**Rationale**: Flask's built-in test client issues HTTP requests in-process (no network socket needed), making tests fast and deterministic. `client.get("/")` returns a response object with `.status_code` and `.data` for clean assertions. This covers FR-001 (greeting content), FR-002 (status 200), and FR-007 (status 404 for unknown routes).

**TDD cycle**:
1. Write `tests/test_app.py` with failing tests (app module does not exist yet). Commit.
2. Implement `app.py`. Tests pass. Commit.
3. Ruff lint + format check. Refactor if needed.

**Alternatives considered**:
- `requests` against a live server: Requires starting a process; slower, less deterministic in CI.
- `unittest.TestCase` subclass: More verbose than pytest; no benefit here.

---

## Finding 7 — README Requirements

**Decision**: `README.md` at repository root using Markdown (consistent with project conventions)

**Rationale**: FR-003 through FR-006 define README content. The spec assumes Markdown format, consistent with repository conventions. Content must cover: project description (FR-004), prerequisites (FR-006), and step-by-step install + run instructions (FR-005). SC-002 targets 5-minute onboarding from README alone.

**Alternatives considered**:
- `README.rst`: Not consistent with project conventions.
- Multiple documentation files: Over-engineered for a single-service hello-world project.

---

## Finding 8 — Linting and Formatting

**Decision**: `ruff` (consistent with existing project toolchain from feature 001)

**Rationale**: Ruff is already in use for feature 001. No reason to introduce a second tool. Commands extend naturally to cover `app.py` and `tests/test_app.py`.

**Commands**:
```bash
ruff check app.py tests/
ruff format --check app.py tests/
```

---

## Summary: All NEEDS CLARIFICATION Items Resolved

| Item | Resolution |
|------|------------|
| Web framework | Flask 2.x |
| Response format | Plain HTML string; `Content-Type: text/html` |
| 404 handling | Custom `@app.errorhandler(404)` returning `"Not Found", 404` |
| Port | 5000 (Flask default); overridable via `PORT` env var |
| Python version | 3.8+ (consistent with project) |
| Testing framework | pytest + Flask test client |
| README format | Markdown at repository root |
| Linter/formatter | ruff (existing toolchain) |
