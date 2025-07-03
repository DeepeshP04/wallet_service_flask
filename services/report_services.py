from models import Wallet, Hold, OperationLog
from extensions import db

def get_wallet_balance(user_id):
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    return wallet, None

def get_hold_report(user_id):
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    active_count = Hold.query.filter_by(wallet_id=wallet.id, status='active').count()
    released_count = Hold.query.filter_by(wallet_id=wallet.id, status='released').count()
    reversed_count = Hold.query.filter_by(wallet_id=wallet.id, status='reversed').count()
    result = {
        'active': active_count,
        'released': released_count,
        'reversed': reversed_count
    }
    return result, None