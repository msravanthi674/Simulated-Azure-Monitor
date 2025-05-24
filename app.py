from flask import Flask
from prometheus_client import Counter, generate_latest
import logging

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

# Logging setup
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    app.logger.info("Home page accessed")
    return "Hello from monitored app!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
