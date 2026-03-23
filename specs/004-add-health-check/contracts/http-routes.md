# HTTP Route Contracts: Simple HTML Navigation

**Branch**: `004-add-health-check` | **Date**: 2026-03-23

## Overview

This document defines the HTTP interface contracts for the Flask web application after the navigation feature is added. All routes return `text/html` responses rendered from Jinja2 templates.

---

## GET /

**Endpoint name**: `index`
**Handler**: `app.index()`

### Request

```
GET / HTTP/1.1
```

No query parameters, headers, or body required.

### Response

| Field | Value |
|-------|-------|
| Status | `200 OK` |
| Content-Type | `text/html; charset=utf-8` |

**Body contract**:
- MUST contain a `<nav>` element.
- MUST contain a link to `/` (Home) with `aria-current="page"`.
- MUST contain a link to `/about` (About) without `aria-current`.
- MUST contain the Home page body content.

---

## GET /about

**Endpoint name**: `about`
**Handler**: `app.about()`

### Request

```
GET /about HTTP/1.1
```

No query parameters, headers, or body required.

### Response

| Field | Value |
|-------|-------|
| Status | `200 OK` |
| Content-Type | `text/html; charset=utf-8` |

**Body contract**:
- MUST contain a `<nav>` element.
- MUST contain a link to `/about` (About) with `aria-current="page"`.
- MUST contain a link to `/` (Home) without `aria-current`.
- MUST contain the About page body content.

---

## GET /<unknown>

**Endpoint name**: Flask 404 error handler
**Handler**: `app.not_found()`

### Request

```
GET /any-nonexistent-path HTTP/1.1
```

### Response

| Field | Value |
|-------|-------|
| Status | `404 Not Found` |
| Content-Type | `text/html; charset=utf-8` |

**Body contract**:
- MUST contain a `<nav>` element (nav bar still renders on error pages).
- MUST contain a human-readable error message (no raw stack traces, no internal identifiers).
- MUST NOT contain `Traceback` or any Python exception detail.

---

## Nav Bar Invariants (all routes)

These contracts apply to every response across all routes:

1. `<nav aria-label="Main navigation">` MUST be present in every HTML response.
2. Navigation links MUST be generated via `url_for()` (not hardcoded paths).
3. Exactly one link MUST carry `aria-current="page"` — the one matching the current route.
4. All navigation links MUST be functional (return non-5xx responses when followed).
