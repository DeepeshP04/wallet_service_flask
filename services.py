from models import Wallet
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