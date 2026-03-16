<!--
SYNC IMPACT REPORT
==================
Version change: (new) → 1.0.0
Added sections:
  - Core Principles (I–V)
  - Development Workflow
  - Quality Gates
  - Governance
Modified principles: N/A (initial ratification)
Removed sections: N/A (initial ratification)
Templates reviewed:
  - .specify/templates/plan-template.md ✅ aligned (Constitution Check gate present)
  - .specify/templates/spec-template.md ✅ aligned (vertical slicing enforced in User Scenarios)
  - .specify/templates/tasks-template.md ✅ aligned (user-story-per-phase structure matches Principle V)
  - .specify/templates/agent-file-template.md ✅ no constitution references requiring update
Deferred TODOs: none
-->

# Specify Agent Constitution

## Core Principles

### I. Code Quality (NON-NEGOTIABLE)

Code MUST be clean, readable, and maintainable at all times.

- Every function or method MUST have a single, clearly stated responsibility.
- Code MUST pass all linting and formatting checks before a pull request is merged.
- Dead code, commented-out blocks, and unused imports MUST be removed before delivery.
- Unnecessary complexity MUST be justified in the plan.md Complexity Tracking table;
  unjustified complexity MUST be simplified before merge.
- Abstractions MUST serve at least two concrete use cases; one-off helpers are prohibited.
- No security vulnerabilities (OWASP Top 10) may be introduced; any found MUST be fixed
  before the affected task is marked complete.

### II. Testing Standards (NON-NEGOTIABLE)

Tests are first-class artifacts and MUST precede implementation.

- TDD is mandatory: tests MUST be written and confirmed failing before any implementation
  code is authored (Red → Green → Refactor).
- Unit tests MUST cover all business logic and edge cases.
- Integration tests MUST cover every user story's acceptance scenarios end-to-end.
- Contract tests MUST be written for every public API or inter-service boundary introduced.
- A task MUST NOT be marked complete unless all associated tests pass.
- Test coverage MUST meet or exceed the threshold defined in plan.md Technical Context;
  if no threshold is set, a minimum of 80 % line coverage applies.

### III. User Experience Consistency

All user-facing surfaces MUST feel like a single, coherent product.

- Error messages MUST be clear, human-readable, and actionable — no raw stack traces
  or internal identifiers exposed to end users.
- Every new UI pattern MUST be reviewed against existing patterns before implementation;
  novel patterns require explicit approval in the plan.
- Accessibility (WCAG 2.1 AA or platform-equivalent standard) MUST be maintained across
  all interfaces.
- Copy, labels, and terminology MUST be consistent with the established glossary; new
  terms MUST be added to the glossary before use in UI.

### IV. Performance Requirements

Performance goals are first-class requirements, not afterthoughts.

- Performance Goals and Constraints MUST be defined in plan.md Technical Context before
  any implementation begins.
- Features MUST be validated against those goals before the user story is marked done.
- Performance regressions (measured against the defined baseline) MUST be caught and
  resolved before merge; no regression may be shipped without an approved exception.
- Profiling or benchmarking evidence MUST accompany any claim that a performance goal
  has been met.

### V. Vertical User Story Slicing (NON-NEGOTIABLE)

Every unit of work MUST deliver end-to-end value to a real user.

- User stories MUST be sliced vertically — each story spans all layers (data, logic, UI,
  API) required to produce a working, demonstrable outcome.
- Horizontal slicing by technical layer (e.g., "implement all models", "implement all
  APIs") is prohibited.
- Each story MUST be independently implementable, testable, deployable, and
  demonstrable without requiring other stories to be complete.
- Tasks MUST be organised by user story in tasks.md, not by technical layer.
- A story that cannot be independently demonstrated MUST be re-sliced before
  implementation begins.

## Development Workflow

The following steps are mandatory for every feature:

1. **Spec** — Create or update `spec.md` with vertically sliced user stories (Principle V).
2. **Plan** — Author `plan.md`; complete Constitution Check gate before Phase 0 research.
3. **Tasks** — Generate `tasks.md` organised by user story with test tasks preceding
   implementation tasks (Principles II, V).
4. **Implement** — Work story by story, P1 first; validate each story independently
   before proceeding to the next.
5. **Review** — All PRs MUST demonstrate passing tests, linting, and performance
   validation against plan.md targets.

## Quality Gates

The following gates MUST be satisfied before a task or story may be marked complete:

| Gate | Principle | Criterion |
|------|-----------|-----------|
| Linting & formatting | I | Zero linting errors; formatter reports no diff |
| Complexity justified | I | Complexity Tracking table complete if any violation exists |
| Tests written first | II | Commit with failing tests predates implementation commit |
| All tests pass | II | CI green; coverage at or above threshold |
| Performance validated | IV | Benchmark results attached; no regression vs. baseline |
| Story independently testable | V | Story demo-able without sibling stories |

## Governance

This constitution supersedes all other development practices and informal conventions.

- **Amendments** require: (a) a written rationale, (b) a diff to this file, (c) a
  review of all dependent templates for consistency, and (d) a version bump following
  the semantic versioning policy below.
- **Versioning policy**:
  - MAJOR — backward-incompatible removals or redefinitions of existing principles.
  - MINOR — new principle or section added, or material expansion of existing guidance.
  - PATCH — clarifications, wording improvements, or non-semantic refinements.
- **Compliance review** — Every PR review MUST verify that the changes comply with
  all five core principles. Non-compliant code MUST NOT be merged.
- **Runtime guidance** — Use `.specify/templates/agent-file-template.md` for
  project-specific development guidelines generated from feature plans.

**Version**: 1.0.0 | **Ratified**: 2026-03-09 | **Last Amended**: 2026-03-09
