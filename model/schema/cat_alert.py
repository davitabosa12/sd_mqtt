from marshmallow import Schema, fields, post_load
from model.cat_alert import CATAlert, CATAlertType


class CATAlertSchema(Schema):
    timestamp = fields.DateTime()
    alert_type = fields.Enum(CATAlertType)
