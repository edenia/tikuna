import docker
import re
import json
import requests
import os
import threading
import logging
import sys

from os.path import join, dirname
from dotenv import load_dotenv
from threading import Thread, Event

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
client = docker.from_env()

indices = (6,7,8,9,10)
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

TIKUNA_SERVER_URL = os.environ.get("TIKUNA_SERVER_URL")

class LogSensor(threading.Thread):

    def __init__(self, node_name):
        super(LogSensor, self).__init__()
        self.dkg = client.containers.get(node_name).logs(stream = True, follow = True, tail = 10)

    def start_data_stream(self):
        try:
            print("Starting %s log collection..." % client)
            logs_added = 0
            log_list = []
            while True:
                line = next(self.dkg).decode("utf-8")
                if "Tikuna log" in line and "removed" in line:
                    line = ansi_escape.sub('', line)
                    words = line.split()
                    log = [words[0]]
                    log.extend([ words[i].partition('=')[2] for i in indices ])
                    if logs_added > 20:
                        logs_added = 0
                        jsonString = json.dumps(log_list)
                        log_list = []
                        print("Sending log request...")
                        print(TIKUNA_SERVER_URL)
                        try:
                            r = requests.post(TIKUNA_SERVER_URL, json=jsonString)
                            print(f"Status Code: {r.status_code}, Response: {r}")
                        except:
                            print("Connection error!")
                    else:
                        log_list.append(log)
                        logs_added += 1
        except StopIteration:
            print(f'log stream ended for prysm-beacon')

    def run(self):
        self.start_data_stream()

    def stop(self):
        sys.exit(0)
