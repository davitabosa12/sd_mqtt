from flask import render_template, Response
from flask.blueprints import Blueprint
from alarms.util.message_queue import message_queue
from model.schema.cat_alert import CATAlertSchema
from util.event_stream_message import EventStreamMessage

index_bp = Blueprint("root", __name__, url_prefix="/")


@index_bp.route("")
def index():
    return render_template("index.html")


@index_bp.route("alerts", methods=["GET"])
def alerts_sse():
    def stream():
        queue = message_queue.subscribe()
        while True:
            alert = queue.get()
            alert_json = CATAlertSchema().dumps(alert)
            yield str(EventStreamMessage(alert_json, "catalert"))

    return Response(stream(), mimetype="text/event-stream")
