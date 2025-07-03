from models import Wallet, Hold, OperationLog
from extensions import db

def get_wallet_balance(user_id):
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    return wallet, None