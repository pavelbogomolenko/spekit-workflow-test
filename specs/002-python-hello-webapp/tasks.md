# Tasks: Python Hello World Web App

**Input**: Design documents from `/specs/002-python-hello-webapp/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/http-api.md ✓, quickstart.md ✓

**Tests**: Included — TDD is a hard requirement (Constitution Principle II; plan.md: "Tests written first (TDD) using pytest with the Flask test client").

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Exact file paths are included in each task description

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization — create the dependency manifest so all developers install the same versions.

- [X] T001 Create `requirements.txt` at repository root listing `flask>=2.0`, `pytest`, and `ruff`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: The pytest fixture that provides the Flask test client is required before any test can be written. This must exist before US1 test tasks begin.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T002 Create `tests/conftest.py` with a `client` pytest fixture that instantiates the Flask app in test mode and returns `app.test_client()`

**Checkpoint**: `tests/conftest.py` exists with `client` fixture — user story test writing can now begin.

---

## Phase 3: User Story 1 — Access Hello World Web App (Priority: P1) 🎯 MVP

**Goal**: A visitor opens the web app and sees "Hello, World!"; any unknown path returns 404.

**Independent Test**: `pytest tests/` passes; `curl http://localhost:5000/` returns 200 with "Hello, World!"; `curl http://localhost:5000/unknown` returns 404.

### Tests for User Story 1 (TDD — write first, confirm they FAIL before implementing)

> **NOTE: Run `pytest tests/` after T003 and T004 and confirm the tests fail. `app.py` does not exist yet.**

- [X] T003 [P] [US1] Write contract tests for `GET /` — `test_get_root_returns_200` and `test_get_root_contains_greeting` — in `tests/test_app.py`
- [X] T004 [P] [US1] Write contract tests for `GET /unknown` — `test_unknown_path_returns_404` and `test_unknown_path_body_is_human_readable` — in `tests/test_app.py`

### Implementation for User Story 1

- [X] T005 [US1] Implement Flask application object and `GET /` route returning `"Hello, World!"` with status 200 in `app.py`
- [X] T006 [US1] Implement `@app.errorhandler(404)` returning `"Not Found"` with status 404 in `app.py`
- [X] T007 [US1] Add `if __name__ == "__main__"` entry point reading `PORT` from environment (default `5000`) and calling `app.run()` in `app.py`

**Checkpoint**: `pytest tests/` is green; `python app.py` starts the server; browser shows "Hello, World!" at `/`; unknown paths return 404. User Story 1 is independently functional.

---

## Phase 4: User Story 2 — Developer Onboarding via README (Priority: P2)

**Goal**: A new developer reads `README.md` and can set up and run the app locally without external help.

**Independent Test**: Follow only the README instructions from a clean environment — the app starts and the greeting is visible in a browser within 5 minutes (SC-002, SC-003).

### Implementation for User Story 2

- [X] T008 [US2] Create `README.md` at repository root containing: project description (FR-004), prerequisites — Python 3.8+, pip (FR-006), step-by-step install (`pip install flask`) and run (`python app.py`) instructions (FR-005), default URL (`http://localhost:5000`), and note on `PORT` env variable override

**Checkpoint**: A developer following only the README can reach the running application. User Story 2 is independently functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Enforce code quality gates required by the constitution before merge.

- [X] T009 [P] Run `ruff check app.py tests/` and `ruff format --check app.py tests/` — fix any lint or formatting issues in `app.py` and `tests/test_app.py`
- [X] T010 Validate quickstart.md end-to-end: follow the TDD workflow section in `specs/002-python-hello-webapp/quickstart.md` from a clean state and confirm all commands succeed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 completion — **BLOCKS all user stories**
- **User Story phases (Phase 3+)**: All depend on Foundational phase completion
  - US1 and US2 can proceed in parallel once Phase 2 is done (different files)
- **Polish (Phase 5)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 — no dependency on US2
- **User Story 2 (P2)**: Can start after Phase 2 — no dependency on US1 (README is a standalone document)

### Within User Story 1

- T003 and T004 MUST be written and **FAIL** before T005/T006/T007 are implemented
- T005 and T006 can be implemented in the same file sequentially (single file — no parallelism)
- T007 (entry point) requires T005/T006 to be present in `app.py`

### Parallel Opportunities

- T003 and T004 are marked [P] — writing two test functions in separate logical blocks in the same session is safe
- T009 (lint/format) is marked [P] — can run alongside any documentation work
- US1 (Phase 3) and US2 (Phase 4) can be worked on in parallel by different developers

---

## Parallel Example: User Story 1

```bash
# Both test stubs can be written together (separate functions, same file):
Task T003: "Write contract tests for GET / in tests/test_app.py"
Task T004: "Write contract tests for GET /unknown in tests/test_app.py"

# Confirm both fail before implementing:
pytest tests/  # expected: 2 errors (ImportError — app.py does not exist)

# Then implement sequentially:
Task T005 → Task T006 → Task T007
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002) — **CRITICAL**
3. Write failing tests (T003, T004) — confirm they fail
4. Complete Phase 3: User Story 1 (T005, T006, T007)
5. **STOP and VALIDATE**: `pytest tests/` green; app runs; browser shows "Hello, World!"
6. Demo / merge if ready

### Incremental Delivery

1. Setup + Foundational → foundation ready
2. US1 → test independently → **MVP delivered** (greeting web app working)
3. US2 → test independently → full feature delivered (README onboarding complete)
4. Polish → lint/format clean → ready for merge

---

## Notes

- [P] tasks = different files or independent logical units with no blocking dependency
- [Story] label maps each task to its user story for traceability
- TDD is mandatory: tests MUST be written and failing before implementation begins
- Commit after each task or logical group
- Stop at each checkpoint to validate the story independently
- `app.py` and `tests/test_app.py` are the only source files — no `src/` package layer needed
