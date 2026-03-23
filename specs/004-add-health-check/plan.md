# Implementation Plan: Simple HTML Navigation

**Branch**: `004-add-health-check` | **Date**: 2026-03-23 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-add-health-check/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Add a consistent HTML navigation bar to every page of the Flask web application, using Jinja2 template inheritance so the nav renders identically across all routes and visually highlights the currently active page — no JavaScript required.

## Technical Context

**Language/Version**: Python 3.8+ with Flask 2.x
**Primary Dependencies**: Flask 2.x, Jinja2 (bundled with Flask)
**Storage**: N/A
**Testing**: pytest
**Target Platform**: Local dev / Linux server
**Project Type**: web-service
**Performance Goals**: Sub-100 ms page load on local dev; no measurable regression vs. baseline
**Constraints**: No JavaScript (FR-005); WCAG 2.1 AA accessibility (aria-current, semantic `<nav>`)
**Scale/Scope**: 2 pages (Home `/`, About `/about`)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Linting & formatting | PASS | ruff enforced; no new lint rules needed |
| Complexity justified | PASS | No novel abstractions; Jinja2 template inheritance is a standard single-use mechanism already provided by Flask |
| Tests written first | PASS | TDD required — failing tests before implementation (Principle II) |
| All tests pass | PASS (pending) | Must be green before story marked done |
| Performance validated | PASS | HTML template rendering is trivially fast; baseline test response time already sub-100 ms |
| Story independently testable | PASS | Each user story has independent acceptance tests |

No constitution violations detected. No entry in Complexity Tracking required.

## Project Structure

### Documentation (this feature)

```text
specs/004-add-health-check/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
app.py                    # Flask app — add /about route, switch to render_template
templates/
├── base.html             # Shared layout with <nav> bar
├── index.html            # Home page — extends base.html
└── about.html            # About page — extends base.html

tests/
├── conftest.py           # Existing Flask test client fixture
├── test_app.py           # Existing + new navigation acceptance tests
└── test_hello.py         # Existing (unchanged)
```

**Structure Decision**: Single-project layout. Templates live in Flask's default `templates/` directory alongside the existing `app.py`. No new top-level directories beyond `templates/` are required.

## Complexity Tracking

> No violations — table left blank intentionally.
