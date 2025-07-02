from extensions import db
from datetime import datetime

class Wallet(db.Model):
    __tablename__ = 'wallet'
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3), nullable=False, default='INR')
    balance = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    holds = db.relationship('Hold', backref='wallet', lazy=True)

class Hold(db.Model):
    __tablename__ = 'hold'
    id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallet.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    released_at = db.Column(db.DateTime, nullable=True)
    reversed_at = db.Column(db.DateTime, nullable=True)

class OperationLog(db.Model):
    __tablename__ = 'operation_log'
    id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallet.id'), nullable=False)
    hold_id = db.Column(db.Integer, db.ForeignKey('hold.id'), nullable=True)
    operation = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
