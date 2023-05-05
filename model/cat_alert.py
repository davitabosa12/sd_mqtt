from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class CATAlertType(Enum):
    HIGH_TEMPERATURE = "high_temp"
    SUDDEN_TEMPERATURE_RAISE = "sudden_temp_raise"


@dataclass
class CATAlert:
    timestamp: datetime
    alert_type: CATAlertType
