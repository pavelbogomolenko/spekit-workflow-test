# Data Model: Simple HTML Navigation

**Branch**: `004-add-health-check` | **Date**: 2026-03-23

## Overview

This feature introduces no persistent data model. All "data" is structural: the set of pages and their route/endpoint definitions. These are captured here as a design artifact.

## Page Registry

Each navigable page is defined by three attributes used by `base.html` to render nav links and detect the active page.

| Field | Type | Description |
|-------|------|-------------|
| `label` | string | Human-readable link text displayed in the nav bar |
| `endpoint` | string | Flask endpoint name (function name registered with `@app.route`) |
| `url` | string | URL path served by this route |

### Pages (v1)

| label | endpoint | url |
|-------|----------|-----|
| Home | `index` | `/` |
| About | `about` | `/about` |

## Template Entities

### `base.html`

Shared layout template. Contains the `<nav>` block that iterates over the page registry (hardcoded inline for simplicity — no dynamic page registry needed at this scale).

**Inputs** (from Flask request context):
- `request.endpoint` — used to determine which nav link is active

**Outputs**: Full HTML document with nav bar and `{% block content %}` slot.

### `index.html`

Extends `base.html`. Fills `{% block content %}` with the Home page body.

### `about.html`

Extends `base.html`. Fills `{% block content %}` with the About page body.

### `404.html`

Extends `base.html`. Fills `{% block content %}` with a human-readable "Page Not Found" message.

## State Transitions

No state transitions — this is a stateless, read-only navigation feature. The only "state" is which page is currently active, derived from `request.endpoint` at render time.

## Validation Rules

- All nav links MUST use `url_for()` to generate URLs (prevents hardcoded path fragility).
- `aria-current="page"` MUST be set on the active link and absent on all others.
- The `<nav>` element MUST appear in `base.html` only (single source of truth).
