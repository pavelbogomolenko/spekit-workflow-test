# Contract: GET /health

**Service**: Flask Web Application
**Feature**: 003-add-health-check
**Version**: 1.0.0

## Endpoint

```
GET /health
```

## Request

| Property        | Value  |
|----------------|--------|
| Method         | GET    |
| Authentication | None   |
| Request Body   | None   |
| Headers        | None required |

## Response (Healthy)

**Status**: `200 OK`

**Headers**:
```
Content-Type: application/json
```

**Body**:
```json
{"status": "ok"}
```

## Response (Error)

If the application encounters an internal error that prevents it from serving requests, Flask will return a standard 500 response. This signals an unhealthy state to load balancers.

**Status**: `500 Internal Server Error`

## Response (Method Not Allowed)

**Status**: `405 Method Not Allowed`

Returned automatically by Flask for any non-GET request to this endpoint.

## Contract Rules

1. The `status` field MUST always be present in the response body on HTTP 200.
2. The response MUST use `Content-Type: application/json`.
3. The endpoint MUST NOT require any authentication headers or cookies.
4. The endpoint MUST respond within 1 second under normal operating conditions (SC-001).
5. Load balancers and monitoring tools MAY determine health from the HTTP status code alone, without parsing the body (SC-003).

## Test Contract

Any implementation MUST satisfy the following observable assertions:

- `GET /health` → 200, `Content-Type: application/json`, body contains `{"status": "ok"}`
- `POST /health` → 405
- `DELETE /health` → 405
- No `Authorization` header required for any request
