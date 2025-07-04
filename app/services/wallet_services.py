from app.models import Wallet, Hold, OperationLog
from app.extensions import db
from datetime import datetime, timedelta

def init_wallet(user_id, currency):
    # Check for existing wallet
    # Initialize wallet, if not exists
    existing_wallet = Wallet.query.filter_by(user_id=user_id).first()
    if existing_wallet:
        return None, "Wallet already exists"

    wallet = Wallet(user_id=user_id, currency=currency)
    db.session.add(wallet)
    db.session.commit()
    return wallet, None

def add_money_to_wallet(user_id, amount):
    # Check if wallet exists or not and return if not exist
    # Else increase the wallet balance by amount.
    # Create operation log
    wallet = Wallet.query.get(user_id)
    if not wallet:
        return None, "Wallet not found"

    wallet.balance += amount
    log = OperationLog(wallet_id=wallet.id, operation="add_money", amount=amount)
    db.session.add(log)
    db.session.commit()
    return wallet, None

def hold_money(user_id, amount):
    # Validate wallet exists and belongs to user
    # Deduct from balance and create hold
    # Create operation log
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if not wallet:
        return None, "Wallet not found"
    if wallet.balance < amount:
        return None, "Insufficient balance to hold"
    wallet.balance -= amount
    hold = Hold(wallet_id=wallet.id, amount=amount, status='active')
    db.session.add(hold)
    log = OperationLog(wallet_id=wallet.id, hold_id=hold.id, operation="hold_money", amount=amount)
    db.session.add(log)
    db.session.commit()
    return hold, None

def release_hold():
    # Check for all active holds for 10 or more minutes.
    # Release the hold and update status to released and update released_at
    # Create operation log.
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
                log = OperationLog(wallet_id=wallet.id, operation="release_hold", amount=hold.amount, hold_id=hold.id)
                db.session.add(log)
                released_count += 1
        db.session.commit()
    return released_count

def reverse_hold(user_id, hold_id):
    # Check for hold and active status
    # Reverse the held funds to the wallet
    # Update hold status and reversed_at time
    # Create operation log
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
    log = OperationLog(wallet_id=wallet.id, operation="reverse_hold", amount=hold.amount, hold_id=hold.id)
    db.session.add(log)
    db.session.commit()
    return hold, None