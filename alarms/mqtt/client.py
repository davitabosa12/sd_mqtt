import asyncio
from datetime import datetime
import logging
import paho.mqtt.client as mqtt
from model.schema.temperature_message import (
    TemperatureMessageSchema,
    TemperatureMessage,
)
from model.schema.cat_alert import CATAlert, CATAlertSchema, CATAlertType
from alarms.util.message_queue import message_queue


def handle_alerts(alert: CATAlert):
    message_queue.publish(alert)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("boiler")
    client.subscribe("boiler/cat")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg_str = msg.payload.decode()
    if msg.topic == "boiler":
        temp: TemperatureMessage = TemperatureMessageSchema().loads(msg_str)
    elif msg.topic == "boiler/cat":
        alert: CATAlert = CATAlertSchema().loads(msg_str)
        handle_alerts(alert)
    print(msg.topic + " " + str(msg.payload.decode()))


_client = mqtt.Client()
_client.on_connect = on_connect
_client.on_message = on_message


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
def start_client():
    _client.connect("192.168.18.118", 1883, 60)
    _client.loop_start()


def stop_client():
    _client.loop_stop()
