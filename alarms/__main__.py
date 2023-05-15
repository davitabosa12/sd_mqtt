import sys

sys.path.append(".")
from server.server import start_server, start_server_async
from mqtt.client import start_client

start_client()
start_server_async()
