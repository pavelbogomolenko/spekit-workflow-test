# Tasks: Simple HTML Navigation

**Input**: Design documents from `/specs/004-add-health-check/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/http-routes.md ✅, quickstart.md ✅

**Tests**: Included — TDD required by project constitution (Principle II). Write failing tests before each implementation task.

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Exact file paths included in all descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the templates directory structure required by the Flask app before any template files are created.

- [X] T001 Create `templates/` directory with placeholder files `templates/base.html`, `templates/index.html`, `templates/about.html`, `templates/404.html` (empty stubs) per plan.md project structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core shared layout and nav-bar invariant tests that ALL user stories depend on. Must be complete before any story can be implemented or tested.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T002 Create `templates/base.html`: full HTML document with `<nav aria-label="Main navigation">` containing `<ul>/<li>/<a>` links for Home (`url_for('index')`) and About (`url_for('about')`), active-link detection via `request.endpoint` (adds `class="active"` and `aria-current="page"` to the matching link), `{% block content %}{% endblock %}` slot, and inline `<style>` for active state (`font-weight: bold; text-decoration: underline`) plus `flex-wrap: wrap` responsive rule in `templates/base.html`
- [X] T003 Write failing nav-bar invariant tests in `tests/test_app.py`: verify that GET `/`, GET `/about`, and GET `/does-not-exist` each return an HTML response containing exactly one `<nav aria-label="Main navigation">` element (these tests MUST fail before Phase 3 implementation begins)

**Checkpoint**: `templates/base.html` exists with correct nav structure; invariant tests are written and failing — user story work can now begin.

---

## Phase 3: User Story 1 — Navigate Between Pages (Priority: P1) 🎯 MVP

**Goal**: A visitor sees a navigation bar on every page and can click links to move between Home (`/`) and About (`/about`); the current page link is visually distinguished.

**Independent Test**: `pytest tests/test_app.py` — GET `/` returns 200 with Home `aria-current="page"` and a link to `/about`; GET `/about` returns 200 with About `aria-current="page"` and a link to `/`.

### Tests for User Story 1

> **NOTE: Write these tests FIRST and confirm they FAIL before implementing T006–T008**

- [X] T004 [US1] Write failing test in `tests/test_app.py`: GET `/` returns status 200, response HTML contains `aria-current="page"` on the Home link, and contains a link whose `href` resolves to `/about`
- [X] T005 [US1] Write failing test in `tests/test_app.py`: GET `/about` returns status 200, response HTML contains `aria-current="page"` on the About link, and contains a link whose `href` resolves to `/`

### Implementation for User Story 1

- [X] T006 [US1] Update `app.py`: change `index()` to `return render_template('index.html')` and add `about()` view function decorated with `@app.route('/about')` returning `render_template('about.html')` in `app.py`
- [X] T007 [P] [US1] Create `templates/index.html`: `{% extends 'base.html' %}` with `{% block content %}` containing a heading and brief Home page body text in `templates/index.html`
- [X] T008 [P] [US1] Create `templates/about.html`: `{% extends 'base.html' %}` with `{% block content %}` containing a heading and brief About page body text in `templates/about.html`

**Checkpoint**: At this point, User Story 1 is fully functional — `pytest tests/test_app.py` passes for all US1 tests and the T003 invariant tests for `/` and `/about`.

---

## Phase 4: User Story 2 — Consistent Navigation Across All Pages (Priority: P2)

**Goal**: The nav bar appears identically in structure and position on every page including the 404 error page; the active indicator updates correctly on every route.

**Independent Test**: `pytest tests/test_app.py` — GET `/does-not-exist` returns 404 with `<nav aria-label="Main navigation">` present and no Python traceback in the body; all three routes pass the T003 invariant test.

### Tests for User Story 2

> **NOTE: Write this test FIRST and confirm it FAILS before implementing T010–T011**

- [X] T009 [US2] Write failing test in `tests/test_app.py`: GET `/does-not-exist` returns status 404, response HTML contains `<nav aria-label="Main navigation">`, and does NOT contain the string `Traceback`

### Implementation for User Story 2

- [X] T010 [US2] Add `not_found(e)` 404 error handler in `app.py` using `@app.errorhandler(404)` returning `render_template('404.html'), 404` in `app.py`
- [X] T011 [P] [US2] Create `templates/404.html`: `{% extends 'base.html' %}` with `{% block content %}` containing a human-readable "Page Not Found" heading and message (no stack traces, no internal identifiers) in `templates/404.html`

**Checkpoint**: All user stories (US1 and US2) are independently functional — `pytest tests/test_app.py` is fully green including T003 invariant tests for all three routes.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, linting, and quickstart scenario walkthrough.

- [X] T012 [P] Run full test suite: `pytest tests/` — all tests must pass green in `tests/`
- [X] T013 [P] Run linting and format checks: `ruff check hello.py app.py tests/` and `ruff format --check hello.py app.py tests/` — zero violations

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — **BLOCKS all user stories**
- **User Stories (Phase 3–4)**: All depend on Phase 2 completion
  - US1 and US2 can proceed in priority order (P1 → P2) or in parallel if staffed
- **Polish (Phase 5)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 — no dependency on US2
- **User Story 2 (P2)**: Can start after Phase 2 — logically builds on US1's templates but is independently testable via the 404 route

### Within Each User Story

- Tests (T004/T005, T009) MUST be written and FAIL before implementation
- app.py route changes (T006, T010) before templates (T007/T008, T011) — templates depend on routes being registered
- Story complete and all tests green before moving to the next priority

### Parallel Opportunities

- T007 and T008 (different template files, no mutual dependency) — run in parallel
- T010 (app.py 404 handler) and T011 (templates/404.html) — different files, run in parallel
- T012 and T013 (independent validation commands) — run in parallel

---

## Parallel Example: User Story 1

```bash
# After T006 (app.py updated), launch template tasks in parallel:
Task: "Create templates/index.html extending base.html with Home page content"   # T007
Task: "Create templates/about.html extending base.html with About page content"  # T008
```

## Parallel Example: User Story 2

```bash
# After T009 (failing test written), launch implementation in parallel:
Task: "Add not_found() 404 error handler in app.py"       # T010
Task: "Create templates/404.html extending base.html"     # T011
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001)
2. Complete Phase 2: Foundational (T002–T003)
3. Complete Phase 3: User Story 1 (T004–T008)
4. **STOP and VALIDATE**: `pytest tests/test_app.py` green; manually visit `/` and `/about` per quickstart.md
5. Deploy/demo if ready

### Incremental Delivery

1. Setup + Foundational → shared layout ready
2. Add User Story 1 → working nav between Home and About → **MVP!**
3. Add User Story 2 → nav on 404 page → complete feature
4. Polish → linting, full test run

---

## Notes

- `[P]` tasks = different files, no blocking dependencies between them
- `[US1]`/`[US2]` label maps each task to its user story for traceability
- All templates MUST use `{% extends 'base.html' %}` — nav lives only in `base.html`
- All nav links MUST use `url_for()` — never hardcoded paths (data-model.md validation rule)
- `aria-current="page"` MUST appear on exactly one nav link per page (contracts/http-routes.md invariant)
- Commit after each phase checkpoint to allow easy rollback
