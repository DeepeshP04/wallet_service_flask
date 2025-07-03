from marshmallow import Schema, fields, validate

class WalletRequestSchema(Schema):
    user_id = fields.Int(required=True)
    currency = fields.Str(required=True, validate=validate.Length(equal=3))

class WalletResponseSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    currency = fields.Str()
    balance = fields.Float()

class AddMoneyRequestSchema(Schema):
    user_id = fields.Int(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01, error="Amount must be greater than 0"))

class HoldRequestSchema(Schema):
    user_id = fields.Int(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0.01, error="Amount must be greater than 0"))

class HoldResponseSchema(Schema):
    id = fields.Int()
    wallet_id = fields.Int()
    amount = fields.Float()
    status = fields.Str()
    created_at = fields.DateTime()
    released_at = fields.DateTime(allow_none=True)
    reversed_at = fields.DateTime(allow_none=True)

class ReverseHoldRequestSchema(Schema):
    user_id = fields.Int(required=True)
    hold_id = fields.Int(required=True)

class WalletBalanceRequestSchema(Schema):
    user_id = fields.Int(required=True)

class HoldReportRequestSchema(Schema):
    user_id = fields.Int(required=True)

class HoldReportResponseSchema(Schema):
    active = fields.Int()
    released = fields.Int()
    reversed = fields.Int()

class WalletOperationRequestSchema(Schema):
    user_id = fields.Int(required=True)

class WalletOperationResponseSchema(Schema):
    add = fields.Int()
    hold = fields.Int()