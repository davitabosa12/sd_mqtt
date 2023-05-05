import sys

sys.path.append(".")
from server.server import start_server
from mqtt.client import start_client

start_client()
start_server()
