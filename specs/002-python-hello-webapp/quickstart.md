# Quickstart: Python Hello World Web App

**Branch**: `002-python-hello-webapp` | **Date**: 2026-03-16

## Prerequisites

- Python 3.8 or later installed and accessible as `python` or `python3` on your PATH.
- `pip` available for installing dependencies.
- (Optional, for running tests) `pytest` and `ruff` installed.

Verify Python is available:

```bash
python --version
# or
python3 --version
```

---

## Installing Dependencies

From the repository root:

```bash
pip install flask
```

To also install test and lint tools:

```bash
pip install flask pytest ruff
```

---

## Running the Application

From the repository root:

```bash
python app.py
```

Expected output:

```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

Open `http://localhost:5000` in any web browser. You should see:

```
Hello, World!
```

To use a different port, set the `PORT` environment variable:

```bash
PORT=8080 python app.py
```

Stop the server with `CTRL+C`.

---

## Running the Tests

Run all tests:

```bash
pytest tests/
```

Run linting and format checks:

```bash
ruff check app.py tests/
ruff format --check app.py tests/
```

Run everything together:

```bash
pytest tests/ && ruff check app.py tests/ && ruff format --check app.py tests/
```

---

## Verifying 404 Behaviour

With the app running, visit `http://localhost:5000/unknown` in a browser or via curl:

```bash
curl -i http://localhost:5000/unknown
# HTTP/1.1 404 NOT FOUND
# ...
# Not Found
```

---

## TDD Workflow (for contributors)

1. Write failing tests in `tests/test_app.py` and confirm they fail:
   ```bash
   pytest tests/  # should fail — app.py does not exist yet
   ```
2. Implement `app.py`.
3. Confirm tests pass:
   ```bash
   pytest tests/
   ```
4. Run linting:
   ```bash
   ruff check app.py tests/ && ruff format --check app.py tests/
   ```
5. Verify performance (response must arrive in < 2 s):
   ```bash
   curl -o /dev/null -s -w "%{time_total}s\n" http://localhost:5000/
   # should be well under 2s on any local machine
   ```
