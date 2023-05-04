from boiler import BoilerEventGenerator
import time
import asyncio

boiler = BoilerEventGenerator()

asyncio.run(boiler.start_boiler())
