# speckit-agent-spekit-workflow-test-33ac8352 Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-22

## Active Technologies

- Python 3.8+ (001-python-hello-world)
- Python 3.8+ + Flask 2.x (002-python-hello-webapp)

## Project Structure

```text
hello.py
app.py
README.md
tests/
```

## Commands

```bash
pytest tests/ && ruff check hello.py app.py tests/ && ruff format --check hello.py app.py tests/
```

## Code Style

Python: Follow standard conventions (PEP 8); enforced by ruff.

## Recent Changes
- 003-add-health-check: Added Python 3.8+ + Flask 2.x

- 002-python-hello-webapp: Added Python 3.8+ + Flask 2.x
- 001-python-hello-world: Added Python 3.8+

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
