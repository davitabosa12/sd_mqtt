from flask import Flask
from server.blueprints import pages

app = Flask(__name__)


def create_app():
    app.register_blueprint(pages.index_bp)
    return app
