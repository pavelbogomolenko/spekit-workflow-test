# Research: Python Hello World App

**Branch**: `001-python-hello-world` | **Date**: 2026-03-16

## Overview

Phase 0 research for a single-file Python "Hello, World!" script. All Technical Context fields were deterministic given the spec; this document records the reasoning and confirms there are no NEEDS CLARIFICATION items.

---

## Finding 1 — Python Version Target

**Decision**: Python 3.8+

**Rationale**: Python 3.8 is the oldest release still in common use on enterprise and developer machines (3.7 reached EOL in June 2023). The feature uses only `print()` and `sys.exit()`, both of which are unchanged since Python 2. Targeting 3.8+ gives the broadest compatibility with no syntax restrictions.

**Alternatives considered**:
- Python 3.11+ (latest stable): Would improve startup performance, but the spec already satisfies the < 1 s goal with any 3.x release. No reason to restrict users.
- Python 3.6/3.7: EOL; no benefit in targeting unsupported runtimes.

---

## Finding 2 — Entry Point File Name

**Decision**: `hello.py`

**Rationale**: `hello.py` is the universal convention for a Python "Hello, World!" program. It is self-documenting, instantly recognisable, and matches the user scenario ("run the application"). The spec requires a single runnable file (FR-004).

**Alternatives considered**:
- `main.py`: Common for larger packages; implies a project structure that does not exist here.
- `app.py`: Implies a web or service application.
- `__main__.py`: Requires a package directory; over-engineered for a one-file script.

---

## Finding 3 — Testing Approach

**Decision**: pytest with `capsys` fixture for output capture; no subprocess needed.

**Rationale**: `capsys` captures `sys.stdout` writes in-process, making tests fast and deterministic. Because the implementation will call `print()` (which writes to `sys.stdout`), `capsys.readouterr().out` captures it cleanly. Exit-code behaviour (FR-002) is verified by confirming no exception is raised and the function returns normally (or by calling `sys.exit(0)` and asserting `SystemExit(0)`).

**Alternatives considered**:
- `subprocess.run(["python", "hello.py"])` + checking `returncode` and `stdout`: Valid integration test, but slower and less portable. Acceptable as a secondary test; not needed as the primary approach.
- `unittest` with `io.StringIO`: More verbose than pytest; no benefit here.
- `mock.patch("builtins.print")`: Verifies the call but not the actual output string; inferior to capsys for FR-001/FR-003 validation.

**TDD cycle**:
1. Write `tests/test_hello.py` — test fails (no `hello.py` yet). Commit.
2. Write `hello.py` with `print("Hello, World!")`. Test passes. Commit.
3. Ruff lint + format check. Refactor if needed.

---

## Finding 4 — Linting and Formatting

**Decision**: `ruff` for both linting and formatting.

**Rationale**: Ruff is the de-facto standard for Python linting/formatting in 2024–2026, replacing flake8 + black in most new projects. It runs in milliseconds on a single file.

**Alternatives considered**:
- flake8 + black: The classic combo, but ruff supersedes both.
- pylint: Too verbose for a one-line script.
- No linting: Violates Constitution Principle I.

**Commands**:
```bash
ruff check hello.py tests/
ruff format --check hello.py tests/
```

---

## Finding 5 — No Contracts Directory Needed

**Decision**: Skip `contracts/` entirely.

**Rationale**: The spec is a purely internal CLI script. It has no public API, no inter-service boundary, no library interface, and no protocol to document. Constitution Principle V and the plan template both confirm contracts are required only for projects that expose external interfaces.

---

## Finding 6 — Performance Baseline

**Decision**: Baseline is cold-start Python interpreter launch; target < 500 ms.

**Rationale**: SC-001 requires execution in < 1 second. A typical CPython 3.8+ cold-start on commodity hardware is 30–150 ms. Even on slow CI runners the baseline is well under 500 ms. No profiling tooling is required; the constraint is trivially satisfied.

**Validation method**: `time python hello.py` during implementation review.

---

## Summary: All NEEDS CLARIFICATION Items Resolved

| Item | Resolution |
|------|-----------|
| Python version | 3.8+ |
| File name | `hello.py` |
| Testing framework | pytest + capsys |
| Linter/formatter | ruff |
| Contracts | Not applicable |
| Performance baseline | < 500 ms cold-start; goal < 1 s |
