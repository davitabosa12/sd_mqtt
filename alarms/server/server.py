from werkzeug import run_simple
from server.app import create_app


def start_server():
    run_simple("localhost", 3456, create_app())
