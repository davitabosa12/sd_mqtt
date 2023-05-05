from marshmallow import Schema, fields, post_load
from model.temperature_message import TemperatureMessage


class TemperatureMessageSchema(Schema):
    timestamp = fields.DateTime()
    temperature = fields.Number()

    @post_load
    def post_load(self, data, **kwargs):
        return TemperatureMessage(data["timestamp"], data["temperature"])
