import docker

client = docker.from_env()
dkg = client.containers.get("prysm-beacon").logs(stream = True, follow = False)
try:
    while True:
        line = next(dkg).decode("utf-8")
        print(line)
except StopIteration:
    print(f'log stream ended for {container_name}')
