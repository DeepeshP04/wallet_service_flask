from models import Wallet, Hold
from extensions import db

def init_wallet(user_id, currency):
    existing_wallet = Wallet.query.filter_by(user_id=user_id).first()
    if existing_wallet:
        return None, "Wallet already exists"

    wallet = Wallet(user_id=user_id, currency=currency)
    db.session.add(wallet)
    db.session.commit()
    return wallet, None

def add_money_to_wallet(user_id, amount):
    wallet = Wallet.query.get(user_id)
    if not wallet:
        return None, "Wallet not found"

    wallet.balance += amount
    db.session.commit()
    return wallet, None

def hold_money(user_id, amount):
    # Validate wallet exists and belongs to user
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    if wallet.balance < amount:
        return None, "Insufficient balance to hold"
    # Deduct from balance and create hold
    wallet.balance -= amount
    hold = Hold(wallet_id=wallet.id, amount=amount, status='active')
    db.session.add(hold)
    db.session.commit()
    return hold, None