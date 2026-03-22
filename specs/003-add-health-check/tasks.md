# Tasks: Add Healthcheck Page

**Input**: Design documents from `/specs/003-add-health-check/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/health-endpoint.md ✓, quickstart.md ✓

**Tests**: Included — TDD enforced per constitution check (plan.md Section: Constitution Check).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the new test file with shared fixture needed by both user stories.

- [X] T001 Create tests/test_health.py with Flask test client fixture (import app from app.py, define `client` pytest fixture using `app.test_client()`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: No foundational tasks required — the existing Flask application in app.py is the complete foundation for this feature. Phase 1 completion unblocks all user story work.

**Checkpoint**: tests/test_health.py exists with client fixture → user story work can begin.

---

## Phase 3: User Story 1 — Operators Check Application Status (Priority: P1) 🎯 MVP

**Goal**: Add a `GET /health` endpoint to app.py that returns HTTP 200 with `{"status": "ok"}` and `Content-Type: application/json`, enabling operators, monitoring tools, and load balancers to verify application liveness.

**Independent Test**: `pytest tests/test_health.py` — verify `GET /health` returns 200, correct JSON body, and correct Content-Type header.

> **TDD: Write tests first and confirm they FAIL before implementing.**

### Tests for User Story 1

- [X] T002 [US1] Write failing test `test_health_returns_200` asserting GET /health → status code 200 in tests/test_health.py
- [X] T003 [US1] Write failing test `test_health_returns_json_status_ok` asserting response body equals `{"status": "ok"}` in tests/test_health.py
- [X] T004 [US1] Write failing test `test_health_content_type_is_json` asserting `Content-Type: application/json` header in tests/test_health.py

### Implementation for User Story 1

- [X] T005 [US1] Add `GET /health` route to app.py using `jsonify({"status": "ok"})` returning HTTP 200 — confirm T002, T003, T004 now pass

**Checkpoint**: `pytest tests/test_health.py::test_health_returns_200 tests/test_health.py::test_health_returns_json_status_ok tests/test_health.py::test_health_content_type_is_json` all pass. User Story 1 is fully functional.

---

## Phase 4: User Story 2 — Automated Deployment Validation (Priority: P2)

**Goal**: Verify the `/health` endpoint satisfies deployment pipeline requirements: accessible without authentication, distinguishable by status code alone, and returns 405 for non-GET methods.

**Independent Test**: `pytest tests/test_health.py` — verify no-auth access and method enforcement behaviour.

> **TDD: Write tests first and confirm they FAIL before implementing.**

### Tests for User Story 2

- [X] T006 [US2] Write failing test `test_health_no_auth_required` asserting GET /health succeeds with no Authorization header in tests/test_health.py
- [X] T007 [US2] Write failing test `test_health_post_returns_405` asserting POST /health → 405 in tests/test_health.py
- [X] T008 [US2] Write failing test `test_health_delete_returns_405` asserting DELETE /health → 405 in tests/test_health.py

### Implementation for User Story 2

- [X] T009 [US2] Confirm T006 passes without code change (no auth is already the default in app.py)
- [X] T010 [US2] Confirm T007 and T008 pass — Flask returns 405 automatically for non-GET methods; no code change needed. If not, restrict route to `methods=["GET"]` in the `/health` route decorator in app.py.

**Checkpoint**: All 8 tests pass. `pytest tests/test_health.py` green. User Stories 1 and 2 are both independently functional.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Validate end-to-end behaviour and ensure lint/format compliance.

- [X] T011 [P] Run full test suite and linting: `pytest tests/ && ruff check app.py tests/test_health.py && ruff format --check app.py tests/test_health.py`
- [X] T012 Run quickstart.md validation: start app with `python app.py`, then `curl http://localhost:5000/health` and confirm response is `{"status": "ok"}` with HTTP 200

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: N/A for this feature
- **User Story phases (Phase 3 & 4)**: Depend on Phase 1 completion (tests/test_health.py must exist)
  - US1 and US2 can proceed sequentially (US1 first, then US2 — US2 tests verify existing implementation)
- **Polish (Phase 5)**: Depends on all user story phases being complete

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Phase 1 only — no other story dependencies
- **User Story 2 (P2)**: Depends on Phase 1 and benefits from US1 implementation being in place (tests verify the same endpoint from a deployment-pipeline perspective)

### Within Each User Story

- Tests MUST be written and confirmed FAILING before implementation
- All US1 tests (T002–T004) can be written sequentially (same file)
- Implementation (T005) follows all US1 tests
- All US2 tests (T006–T008) can be written sequentially (same file)
- Verification tasks (T009–T010) follow US2 tests

### Parallel Opportunities

- T011 (lint/format) is marked [P] — can run alongside manual quickstart validation
- US1 tests T002–T004 are small and sequential within one file; no parallelism benefit

---

## Parallel Example: User Story 1

```bash
# Write all three failing tests first (sequential — same file):
Task: T002 "Write failing test test_health_returns_200 in tests/test_health.py"
Task: T003 "Write failing test test_health_returns_json_status_ok in tests/test_health.py"
Task: T004 "Write failing test test_health_content_type_is_json in tests/test_health.py"

# Then implement:
Task: T005 "Add GET /health route in app.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Create tests/test_health.py with client fixture
2. Complete Phase 3: Write failing tests → implement `/health` route → confirm tests pass
3. **STOP and VALIDATE**: `pytest tests/test_health.py` all green; `curl http://localhost:5000/health` returns `{"status": "ok"}`
4. Deploy/demo if ready

### Incremental Delivery

1. Phase 1 → test file scaffolding ready
2. Phase 3 (US1) → `/health` endpoint live and tested → MVP deployable
3. Phase 4 (US2) → deployment-pipeline behaviour verified (no additional code changes expected)
4. Phase 5 → lint/format clean, quickstart validated

---

## Notes

- [P] tasks = different files or no file conflicts, can run in parallel
- [Story] label maps each task to a specific user story for traceability
- Both user stories share the same `/health` endpoint; US2 verification tasks are primarily test coverage, not new implementation
- TDD enforced: all tests written before implementation, confirmed failing first
- Commit after Phase 3 checkpoint and again after Phase 5 validation
- No new directories required — single file addition (tests/test_health.py) and single file modification (app.py)
