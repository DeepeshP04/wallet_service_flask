from models import Wallet
from extensions import db

def init_wallet():
    wallet = Wallet()
    db.session.add(wallet)
    db.session.commit()
    return wallet

def add_money_to_wallet(wallet_id, amount):
    wallet = Wallet.query.get(wallet_id)
    if not wallet:
        return None, "Wallet not found"

    wallet.balance += amount
    db.session.commit()
    return wallet, None