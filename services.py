from models import Wallet, Hold
from extensions import db
from datetime import datetime, timedelta

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

def release_hold():
    now = datetime.utcnow()
    ten_min_ago = now - timedelta(minutes=10)
    holds = Hold.query.filter(Hold.status == 'active', Hold.created_at <= ten_min_ago).all()
    
    released_count = 0
    if holds:
        for hold in holds:
            wallet = Wallet.query.get(hold.wallet_id)
            if wallet:
                wallet.balance += hold.amount
                hold.status = 'released'
                hold.released_at = now
                released_count += 1
        db.session.commit()
    return released_count

def reverse_hold(user_id, hold_id):
    hold = Hold.query.get(hold_id)
    if not hold:
        return None, "Hold not found"
    if hold.status != 'active':
        return None, "Hold is not active"
    wallet = Wallet.query.get(hold.wallet_id)
    if not wallet:
        return None, "Wallet not found"
    if user_id != wallet.user_id:
        return None, "Hold does not belong to this user"

    wallet.balance += hold.amount
    hold.status = 'reversed'
    hold.reversed_at = datetime.utcnow()
    db.session.commit()
    return hold, None
    