# Quickstart: Python Hello World App

**Branch**: `001-python-hello-world` | **Date**: 2026-03-16

## Prerequisites

- Python 3.8 or later installed and accessible as `python` or `python3` on your PATH.
- (Optional, for running tests) `pytest` and `ruff` installed.

Verify Python is available:

```bash
python --version
# or
python3 --version
```

## Running the Application

From the repository root:

```bash
python hello.py
```

Expected output:

```
Hello, World!
```

Expected exit code: `0`

```bash
python hello.py; echo "Exit code: $?"
# Hello, World!
# Exit code: 0
```

## Running the Tests

Install test dependencies (first time only):

```bash
pip install pytest ruff
```

Run tests:

```bash
pytest tests/
```

Run linting and format checks:

```bash
ruff check hello.py tests/
ruff format --check hello.py tests/
```

Run everything together:

```bash
pytest tests/ && ruff check hello.py tests/ && ruff format --check hello.py tests/
```

## TDD Workflow (for contributors)

1. Write a failing test in `tests/test_hello.py` and confirm it fails:
   ```bash
   pytest tests/  # should fail — hello.py does not exist yet
   ```
2. Implement `hello.py`.
3. Confirm tests pass:
   ```bash
   pytest tests/
   ```
4. Run linting:
   ```bash
   ruff check hello.py tests/ && ruff format --check hello.py tests/
   ```
5. Verify performance:
   ```bash
   time python hello.py
   # real time should be well under 1s
   ```
