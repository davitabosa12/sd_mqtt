from flask.blueprints import Blueprint

index_bp = Blueprint("root", __name__, url_prefix="/")


@index_bp.route("")
def index():
    return "CAT server"
