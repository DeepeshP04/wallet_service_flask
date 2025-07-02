from models import Wallet
from extensions import db

def init_wallet():
    wallet = Wallet()
    db.session.add(wallet)
    db.session.commit()
    return wallet