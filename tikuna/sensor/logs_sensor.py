import docker
import re
import json
import requests

client = docker.from_env()

indices = (6,7,8,9,10)
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

dkg = client.containers.get("prysm-beacon").logs(stream = True, follow = True, tail = 10)
try:
    print("Starting Ethereum log collection...")
    logs_added = 0
    log_list = []
    while True:
        line = next(dkg).decode("utf-8")
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
                try:
                    r = requests.post('http://parsek.io:4444/evaluate', json=jsonString)
                    print(f"Status Code: {r.status_code}, Response: {r}")
                except:
                    print("Connection error!")
            else:
                log_list.append(log)
                logs_added += 1
except StopIteration:
    print(f'log stream ended for prysm-beacon')
