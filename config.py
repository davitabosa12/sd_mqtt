import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")

try:
    PORT = int(os.getenv("MQTT_PORT", 1883))
except:
    PORT = 1883
