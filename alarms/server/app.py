from flask import Flask
from flask_cors import CORS
from server.blueprints import pages

app = Flask(__name__)
CORS(app)


def create_app():
    app.register_blueprint(pages.index_bp)
    return app
