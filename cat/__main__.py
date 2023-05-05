import sys

sys.path.append(".")
from mqtt.client import start_client, stop_client
from server.server import start_server

start_client()
start_server()
