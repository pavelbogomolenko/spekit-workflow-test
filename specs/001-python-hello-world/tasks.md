# Tasks: Python Hello World App

**Input**: Design documents from `/specs/001-python-hello-world/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, quickstart.md ✓

**Tests**: Included — TDD approach required by plan.md (constitution gate: "Tests written first: PASS"). Tests must be written and confirmed to FAIL before implementation.

**Organization**: Single user story (P1). Tasks flow: Setup → User Story 1 (TDD: test-first → implement → verify) → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different concerns, no dependencies on incomplete tasks)
- **[Story]**: Which user story this task belongs to (US1)

---

## Phase 1: Setup

**Purpose**: Create the project directory structure required before any implementation begins.

- [X] T001 Create `tests/` directory at repository root (empty directory for pytest auto-discovery)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: No shared infrastructure required — single-story, stdlib-only feature. No foundational tasks.

**Checkpoint**: Foundation ready — User Story 1 can begin immediately after Phase 1.

---

## Phase 3: User Story 1 - Run Hello World Program (Priority: P1) 🎯 MVP

**Goal**: A developer can run `python hello.py` from the command line and see `Hello, World!` printed to stdout, with the program exiting with code 0.

**Independent Test**: Execute `python hello.py` and verify output is `Hello, World!\n` on stdout and exit code is `0`. Delivers 100% of feature value on its own.

### Tests for User Story 1 (TDD — write FIRST, confirm FAIL before implementing)

> **CRITICAL**: Run `pytest tests/` after T002 and confirm the test FAILS before proceeding to T003.

- [X] T002 [US1] Write failing pytest test using `capsys` fixture for output and exit-code verification in `tests/test_hello.py`

### Implementation for User Story 1

- [X] T003 [US1] Implement `hello.py` with `print("Hello, World!")` at repository root (depends on T002 failing first)
- [X] T004 [US1] Verify all pytest tests pass: `pytest tests/` (depends on T003)

**Checkpoint**: At this point User Story 1 is fully functional and testable. `python hello.py` outputs `Hello, World!` and exits with code 0.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Lint, format, and end-to-end validation to confirm all constitution gates pass.

- [X] T005 [P] Run `ruff check hello.py tests/` and fix any lint errors in `hello.py` and `tests/test_hello.py`
- [X] T006 [P] Run `ruff format --check hello.py tests/` and fix any formatting issues in `hello.py` and `tests/test_hello.py`
- [X] T007 Validate quickstart.md scenarios: run `python hello.py; echo "Exit code: $?"` and confirm output matches expected (`Hello, World!` / `Exit code: 0`)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: N/A for this feature
- **User Story 1 (Phase 3)**: Depends on Phase 1 completion
  - T002 depends on T001 (needs `tests/` directory)
  - T003 depends on T002 FAILING (TDD gate)
  - T004 depends on T003
- **Polish (Phase 4)**: Depends on T004 (all story tasks complete)

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies on other stories — this is the sole story and delivers 100% of feature value.

### Within User Story 1

1. Write test (T002) → confirm it FAILS
2. Implement (T003) → confirm test now PASSES (T004)
3. Polish (T005, T006, T007) — lint and format checks can run in parallel

### Parallel Opportunities

- T005 and T006 (lint and format checks) can run in parallel — independent checks on same files

---

## Parallel Example: User Story 1

```bash
# After T004 passes, run Polish tasks in parallel:
Task T005: ruff check hello.py tests/
Task T006: ruff format --check hello.py tests/
```

---

## Implementation Strategy

### MVP (User Story 1 Only — this IS the full feature)

1. Complete Phase 1: Create `tests/` directory
2. Complete Phase 3: TDD cycle for User Story 1
   - T002: Write failing test → confirm fail
   - T003: Implement `hello.py`
   - T004: Confirm tests pass
3. **STOP and VALIDATE**: Run `python hello.py` — confirm full feature works
4. Complete Phase 4: Polish (lint + format + quickstart validation)

### Incremental Delivery

This feature has a single user story, so there is no incremental delivery beyond the MVP. Each phase checkpoint delivers:

- After T001: Directory structure ready
- After T002: Failing test committed (TDD gate satisfied)
- After T004: Feature complete and tested
- After T007: Constitution all-green, ready to merge

---

## Notes

- [P] tasks = independent concerns, no blocking dependencies between them
- [US1] label maps every task to User Story 1 for traceability
- TDD gate is mandatory (constitution Principle II): T002 must be committed as a failing test before T003 is written
- `ruff` is the sole linting/formatting tool — no flake8, black, or pylint needed
- No `requirements.txt` or `pyproject.toml` needed — stdlib only; pytest/ruff are dev tools only
- Verify performance informally: `time python hello.py` should be well under 1 second
