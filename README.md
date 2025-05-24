# Simulated Azure Monitor

A full local monitoring stack inspired by Azure Monitor using:

- Python (Flask) for app + telemetry
- Prometheus for metrics
- Grafana for dashboards + alerting
- Flask Webhook receiver (simulates Azure action groups)

## Run Locally

```bash
docker-compose up --build
