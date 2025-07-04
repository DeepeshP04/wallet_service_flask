from app.models import Wallet, Hold, OperationLog
from app.extensions import db

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

def get_wallet_operation_report(user_id):
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    add_count = OperationLog.query.filter_by(wallet_id=wallet.id, operation='add_money').count()
    hold_count = OperationLog.query.filter_by(wallet_id=wallet.id, operation='hold_money').count()
    release_count = OperationLog.query.filter_by(wallet_id=wallet.id, operation='release_hold').count()
    reverse_count = OperationLog.query.filter_by(wallet_id=wallet.id, operation='reverse_hold').count()
    result = {
        'add': add_count,
        'hold': hold_count,
        'release': release_count,
        'reverse': reverse_count
    }
    return result, None

# Get hold report for all users
def get_overall_hold_report():
    active_count = Hold.query.filter_by(status='active').count()
    released_count = Hold.query.filter_by(status='released').count()
    reversed_count = Hold.query.filter_by(status='reversed').count()
    result = {
        'active': active_count,
        'released': released_count,
        'reversed': reversed_count
    }
    return result, None

# Get wallet operation report for all users
def get_overall_wallet_operation_report():
    add_count = OperationLog.query.filter_by(operation='add_money').count()
    hold_count = OperationLog.query.filter_by(operation='hold_money').count()
    release_count = OperationLog.query.filter_by(operation='release_hold').count()
    reverse_count = OperationLog.query.filter_by(operation='reverse_hold').count()
    result = {
        'add': add_count,
        'hold': hold_count,
        'release': release_count,
        'reverse': reverse_count
    }
    return result, None