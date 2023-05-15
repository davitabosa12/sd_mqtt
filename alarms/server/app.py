from flask import Flask
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
from server.blueprints import pages

app = Flask(__name__)

CORS(app)


def create_app():
    app.register_blueprint(pages.index_bp)
    return app


asgi_app = WsgiToAsgi(app)
