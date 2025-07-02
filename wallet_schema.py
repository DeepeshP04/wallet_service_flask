from marshmallow import Schema, fields

class WalletResponseSchema(Schema):
    id = fields.Int()
    currency = fields.Str()
    balance = fields.Float()