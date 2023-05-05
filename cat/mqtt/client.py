import asyncio
from datetime import datetime
import logging
import paho.mqtt.client as mqtt
from calcs.CAT import CAT
from model.schema.temperature_message import (
    TemperatureMessageSchema,
    TemperatureMessage,
)
from model.schema.cat_alert import CATAlert, CATAlertSchema, CATAlertType

logger = logging.getLogger("CAT_MQTT_CLIENT")
logger.setLevel(logging.INFO)
cat_event_loop = asyncio.new_event_loop()
cat_lock = asyncio.Lock()
cat = CAT(cat_lock)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("boiler")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "boiler":
        msg_str = msg.payload.decode()
        temp: TemperatureMessage = TemperatureMessageSchema().loads(msg_str)
        asyncio.run(cat.register_temperature(temp))
    print(msg.topic + " " + str(msg.payload.decode()))


_client = mqtt.Client()
_client.on_connect = on_connect
_client.on_message = on_message


def send_alert(msg: CATAlert):
    msg_json = CATAlertSchema().dumps(msg)
    _client.publish("boiler/cat", msg_json)


def on_high_temperature():
    now = datetime.now()
    print(f"High Temp: {now.isoformat()}")
    msg = CATAlert(now, CATAlertType.HIGH_TEMPERATURE)
    send_alert(msg)


def on_sudden_temperature_raise():
    now = datetime.now()
    print(f"Sudden temp raise: {now.isoformat()}")
    msg = CATAlert(now, CATAlertType.HIGH_TEMPERATURE)
    send_alert(msg)


cat.on_high_temperature = on_high_temperature
cat.on_sudden_temperature_raise = on_sudden_temperature_raise


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
def start_client():
    logger.info("Starting MQTT Client")
    _client.connect("192.168.18.118", 1883, 60)
    _client.loop_start()
    cat.start_cat(cat_event_loop)


def stop_client():
    _client.loop_stop()
