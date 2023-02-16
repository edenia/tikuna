import prometheus_client
import random, time
import yaml

from threading import Thread
from prometheus_client import start_http_server, Summary, Gauge, MetricsHandler
from flask import Response, Flask, request
from prometheus_client.core import CollectorRegistry
from collections import Counter

from tikuna.service import EthereumAttackDetector

app = Flask(__name__)

@app.route("/metrics")
def requests_count():
    get_stuck_blocks()
    get_failed_txs()
    get_number_txs()
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

@app.route("/evaluate", methods=['POST'])
def evaluate_log():
    request_data = request.get_json()

    logs = None

    if request_data:
        if 'logs' in request_data:
            if (type(request_data['logs']) == list) and (len(request_data['logs']) > 0):
                logs = request_data['logs'][0]
    res = []
    self.detector = evaluate_logs.evaluate(logs)
    return Response(res, mimetype="text/plain")

if __name__ == "__main__":
    self.detector = EthereumAttackDetector()
    app.run(host="0.0.0.0", port=4444)
