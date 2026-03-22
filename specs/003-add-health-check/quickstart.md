# Quickstart: Add Healthcheck Page

**Feature**: 003-add-health-check

## What this adds

A `/health` endpoint to the Flask app that returns `{"status": "ok"}` with HTTP 200, enabling operators, monitoring tools, and deployment pipelines to verify application liveness.

## Running the app

```bash
pip install flask
python app.py
```

The app starts on port 5000 by default (override with `PORT` env var).

## Calling the health endpoint

```bash
curl http://localhost:5000/health
# {"status": "ok"}
```

Expected response:
- HTTP status: `200`
- Body: `{"status": "ok"}`
- Content-Type: `application/json`

## Running tests

```bash
pytest tests/
```

## Configuring a load balancer (example)

Point your load balancer health probe at:
```
GET http://<host>:<port>/health
```
Expect HTTP 200 as the healthy signal. No authentication headers required.

## Configuring Kubernetes liveness probe (example)

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 3
  periodSeconds: 10
```
