import signal
import time

from subprocess import PIPE
from subprocess import Popen
from subprocess import TimeoutExpired

import requests


def test_serve(port_label):
    # Use a different port for each port label
    # because the OS takes a long time to free
    # up the ports when trying to reuse
    ports = {"-p": 8081, "--port": 8082}
    port = ports.get(port_label, None)

    # build args
    args = []
    if port_label is not None:
        args += [port_label, str(port)]
    command = ["soh", "serve"]
    if len(args) > 0:
        command += args

    # launch in a subprocess
    process = Popen(command, stdout=PIPE)
    # let the server spin up
    time.sleep(3)

    # make a request for the readme file
    p = str(port if port_label is not None else 8080)
    host = f"http://localhost:{p}"
    url = f"{host}/README.rst"
    print(url)
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        process.kill()
        raise

    # terminate the grab stdout to verify
    process.send_signal(signal.SIGINT)
    try:
        outs, _ = process.communicate(timeout=3)
    except TimeoutExpired:
        process.kill()
        outs, _ = process.communicate()

    process.kill()

    assert response.status_code == 200

    assert host in outs.decode()
