# Research: Add Healthcheck Page

**Feature**: 003-add-health-check | **Date**: 2026-03-22

## Findings

### Endpoint Path

- **Decision**: `/health`
- **Rationale**: `/health` is the de-facto standard path used by Kubernetes liveness probes, AWS ALB/NLB, and most load balancers. It is shorter and more conventional than `/healthcheck`. Flask route naming is unambiguous.
- **Alternatives considered**: `/healthcheck` (verbose), `/ping` (less descriptive), `/status` (ambiguous — sometimes used for richer status pages).

### Response Format

- **Decision**: JSON `{"status": "ok"}` with `Content-Type: application/json`
- **Rationale**: Machine-readable, minimal, and matches spec assumption. Using Flask's `jsonify()` ensures correct content-type header automatically. The `status` field is the minimum contract required by spec FR-003.
- **Alternatives considered**: Plain-text `"ok"` (not machine-readable per spec assumption), richer payloads with uptime/version (overkill for a liveness-only check per spec assumption).

### HTTP Status Code

- **Decision**: 200 OK
- **Rationale**: Required by spec FR-002. Load balancers and monitoring tools interpret any non-2xx as unhealthy.
- **Alternatives considered**: 204 No Content (no body, incompatible with FR-003 requiring a response body).

### Authentication

- **Decision**: No authentication
- **Rationale**: Required by spec FR-004. The endpoint must be reachable by load balancers and monitoring tools without credentials.
- **Alternatives considered**: IP allowlisting (out of scope for this feature; infrastructure concern).

### HTTP Methods

- **Decision**: GET only
- **Rationale**: Required by spec FR-006. Flask default route handles GET; non-GET methods return 405 automatically.
- **Alternatives considered**: HEAD in addition to GET (supported implicitly by Flask for free; no code change needed).

### Testing Approach

- **Decision**: pytest with Flask test client
- **Rationale**: Consistent with existing test infrastructure. Flask's built-in test client provides full in-process integration testing without requiring a live server. Contract tests verify the response shape.
- **Alternatives considered**: Live server tests with `requests` (heavier; not needed for a single-service test).

### Performance

- **Decision**: No explicit caching or async handling needed
- **Rationale**: A liveness endpoint that returns a static JSON object will respond well under 1ms, far inside the 1-second SLA defined in FR-005. No optimization required.
