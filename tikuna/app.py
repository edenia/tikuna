import sys
sys.path.append("../")
import prometheus_client
import random, time
import yaml
import os

from os.path import join, dirname
from dotenv import load_dotenv
from threading import Thread
from prometheus_client import start_http_server, Summary, Gauge, MetricsHandler
from flask import Response, Flask, request
from prometheus_client.core import CollectorRegistry
from collections import Counter

from tikuna.service.evaluate_logs_octets import EthereumAttackDetector

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

detector = None
app = Flask(__name__)

@app.route("/evaluate", methods=['POST'])
def evaluate_log():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        logs = request.json
        if logs:
           detector.evaluate(logs)
        res = [""]
        return Response(res, mimetype="text/plain")
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    detector = EthereumAttackDetector()
    app.run(host="0.0.0.0", port=4444)
