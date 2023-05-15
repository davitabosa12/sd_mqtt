from werkzeug import run_simple
from server.app import create_app
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve


def start_server():
    run_simple("localhost", 3456, create_app())


def start_server_async():
    config = Config()
    config.bind = ["127.0.0.1:3456"]
    asyncio.run(serve(create_app(), config))
