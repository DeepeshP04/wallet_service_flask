from marshmallow import Schema, fields, validate

class WalletResponseSchema(Schema):
    id = fields.Int()
    currency = fields.Str()
    balance = fields.Float()

class AddMoneyRequestSchema(Schema):
    wallet_id = fields.Int(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01, error="Amount must be greater than 0"))

class HoldRequestSchema(Schema):
    wallet_id = fields.Int(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01, error="Amount must be greater than 0"))