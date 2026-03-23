# Quickstart: Simple HTML Navigation

**Branch**: `004-add-health-check` | **Date**: 2026-03-23

## Prerequisites

- Python 3.8+
- Flask 2.x installed (`pip install flask`)

## Run the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) — you should see the Home page with a navigation bar at the top.

## Navigate Between Pages

1. Open [http://localhost:5000](http://localhost:5000) — the **Home** link in the nav bar should appear active (bold/underlined).
2. Click **About** in the nav bar — you should land on `/about` with the **About** link now active.
3. Click **Home** — you return to `/` with Home active again.

## Verify the 404 Page

Navigate to any non-existent URL, e.g. [http://localhost:5000/does-not-exist](http://localhost:5000/does-not-exist).

The navigation bar should still appear at the top; the page body should show a human-readable "Page Not Found" message.

## Run Tests

```bash
pytest tests/
```

All tests should pass green. To also check linting and formatting:

```bash
pytest tests/ && ruff check hello.py app.py tests/ && ruff format --check hello.py app.py tests/
```

## Key Files

| File | Purpose |
|------|---------|
| `app.py` | Flask routes — `index()`, `about()`, and `not_found()` |
| `templates/base.html` | Shared layout with `<nav>` bar |
| `templates/index.html` | Home page content |
| `templates/about.html` | About page content |
| `templates/404.html` | Error page content (nav bar still present) |
| `tests/test_app.py` | Acceptance tests covering nav bar invariants |
