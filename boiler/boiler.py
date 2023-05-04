import asyncio
from concurrent.futures import ThreadPoolExecutor
import paho.mqtt.client as mqtt

WAIT_TIME = 60  # seconds
TIMESCALE = 0.016


class Boiler:
    pass


class BoilerEventGenerator:
    def __init__(self) -> None:
        self.loop = asyncio.new_event_loop()
        self.boiler = Boiler()
        self.task = None
        self.client = mqtt.Client()
        self.client.connect("192.168.18.118", 1883, 60)

    async def start_boiler(self):
        await self._boiler_coroutine()

    async def _boiler_coroutine(self):
        while True:
            print("Sending event")
            self.client.publish("test", "hello").wait_for_publish(5)
            await asyncio.sleep(WAIT_TIME * TIMESCALE)
