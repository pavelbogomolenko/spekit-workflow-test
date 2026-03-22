# Data Model: Add Healthcheck Page

**Feature**: 003-add-health-check | **Date**: 2026-03-22

## Overview

This feature introduces no persistent data, no database entities, and no state transitions. The healthcheck endpoint is a stateless liveness probe.

## Response Schema

### HealthResponse

The single response object returned by the `/health` endpoint.

| Field    | Type   | Required | Description                          |
|----------|--------|----------|--------------------------------------|
| `status` | string | Yes      | Application health status indicator. Value is always `"ok"` when the application is running normally. |

**Example**:
```json
{"status": "ok"}
```

**Validation rules**:
- `status` MUST be present in the response body.
- `status` value is `"ok"` for a healthy application.
- `Content-Type` header MUST be `application/json`.

## State Transitions

None. The endpoint is stateless and performs a liveness check only.

## Storage

None. No persistence layer is accessed.
