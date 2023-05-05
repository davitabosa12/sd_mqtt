import asyncio
from datetime import timedelta
from typing import List, Callable
from statistics import mean
from model.temperature_message import TemperatureMessage

WAIT_TIME = 20


class CAT:
    def __init__(self, lock):
        self.temp_buffer: List[TemperatureMessage] = []
        self.on_high_temperature: Callable = None
        self.on_sudden_temperature_raise: Callable = None
        self.lock = lock

    async def register_temperature(self, temperature: TemperatureMessage):
        async with self.lock:
            self.temp_buffer.append(temperature)
            # Truncate list to 100 samples
            if len(self.temp_buffer) > 100:
                del self.temp_buffer[0]

    async def compute_avg_temperature(self):
        while True:
            await asyncio.sleep(WAIT_TIME)
            async with self.lock:
                # Filter all messages in the last 120 secs
                if len(self.temp_buffer) > 2:
                    latest_timestamp = self.temp_buffer[-1].timestamp
                    cutoff_timestamp = latest_timestamp - timedelta(seconds=120)

                    filtered_temps = [
                        t.temperature
                        for t in self.temp_buffer
                        if t.timestamp >= cutoff_timestamp
                    ]
                    self.print_cat_report(
                        filtered_temps, cutoff_timestamp, latest_timestamp
                    )
                    if filtered_temps:
                        mean_temps = mean(filtered_temps)
                        if mean_temps > 200:
                            if callable(self.on_high_temperature):
                                self.on_high_temperature()

                    last_temps_delta = (
                        self.temp_buffer[-1].temperature
                        - self.temp_buffer[-2].temperature
                    )
                    if last_temps_delta > 5:
                        if callable(self.on_sudden_temperature_raise):
                            self.on_sudden_temperature_raise()

    def print_cat_report(self, temps, cutoff_timestamp, latest_timestamp):
        print("********* CAT REPORT **********")
        print(
            f"Timestamp range: {cutoff_timestamp.isoformat()} - {latest_timestamp.isoformat()}"
        )

    def start_cat(self, loop):
        loop.run_until_complete(self.compute_avg_temperature())
