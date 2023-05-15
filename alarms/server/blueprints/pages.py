from flask import render_template, Response
from flask.blueprints import Blueprint
from alarms.util.message_queue import message_queue, temps_message_queue
from model.schema.cat_alert import CATAlertSchema
from model.schema.temperature_message import TemperatureMessageSchema
from util.event_stream_message import EventStreamMessage

index_bp = Blueprint("root", __name__, url_prefix="/")


@index_bp.route("")
def index():
    return render_template("index.html")


@index_bp.route("alerts", methods=["GET"])
async def alerts_sse():
    def stream():
        queue = message_queue.subscribe()
        while True:
            alert = queue.get()
            alert_json = CATAlertSchema().dumps(alert)
            print("Sent catalert event -> ", alert_json)
            yield str(EventStreamMessage(alert_json, "catalert"))

    return Response(stream(), mimetype="text/event-stream")


@index_bp.route("temps", methods=["GET"])
async def temps_sse():
    def stream():
        queue = temps_message_queue.subscribe()
        while True:
            temp = queue.get()
            temp_json = TemperatureMessageSchema().dumps(temp)
            print("Sent temp event -> ", temp_json)
            yield str(EventStreamMessage(temp_json, "temp"))

    return Response(stream(), mimetype="text/event-stream")
