from dataclasses import dataclass
from datetime import datetime


@dataclass
class TemperatureMessage:
    timestamp: datetime
    temperature: float
