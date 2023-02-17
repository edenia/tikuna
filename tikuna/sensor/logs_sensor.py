import docker
import re
import json
import requests

client = docker.from_env()

indices = (6,7,8,9,10)
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

dkg = client.containers.get("prysm-beacon").logs(stream = True, follow = True, tail = 10)
try:
    logs_added = 0
    log_list = []
    while True:
        line = next(dkg).decode("utf-8")
        if "Tikuna log" in line and "removed" in line:
            line = ansi_escape.sub('', line)
            words = line.split()
            log = [words[0]]
            log.extend([ words[i].partition('=')[2] for i in indices ])
            print(log)
            if logs_added > 20:
                logs_added = 0
                jsonString = json.dumps(log_list)
                r = requests.post('http://parsek.io:4444', json=jsonString)
                print(f"Status Code: {r.status_code}, Response: {r.json()}")
            else:
                log_list.extend(log)
                logs_added += 1
except StopIteration:
    print(f'log stream ended for prysm-beacon')
