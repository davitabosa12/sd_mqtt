import asyncio
from datetime import datetime
import math
import paho.mqtt.client as mqtt
import config
from model.schema.temperature_message import (
    TemperatureMessage,
    TemperatureMessageSchema,
)

WAIT_TIME = 60  # seconds
TIMESCALE = 0.016


class Boiler:
    def __init__(self):
        self._temperature = 150
        self.i = 0

    @property
    def temperature(self):
        self._temperature += 70 * math.sin(self.i)
        self.i += 1
        return self._temperature


class BoilerEventGenerator:
    def __init__(self) -> None:
        self.loop = asyncio.new_event_loop()
        self.boiler = Boiler()
        self.task = None
        self.client = mqtt.Client()
        self.client.connect(config.MQTT_BROKER, 1883, 60)

    async def start_boiler(self):
        await self._boiler_coroutine()

    async def _boiler_coroutine(self):
        print("Sending events...")
        while True:
            now = datetime.now()
            msg = TemperatureMessage(now, self.boiler.temperature)
            msg_json = TemperatureMessageSchema().dumps(msg)
            self.client.publish("boiler", msg_json).wait_for_publish(5)
            await asyncio.sleep(WAIT_TIME * TIMESCALE)
