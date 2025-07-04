from flask import Blueprint, jsonify, request
from app.schemas.schema import WalletRequestSchema, WalletResponseSchema, AddMoneyRequestSchema, HoldRequestSchema, HoldResponseSchema, ReverseHoldRequestSchema
from app.services import wallet_services

wallet_bp = Blueprint('wallet', __name__, url_prefix='/wallet')

# Initialize wallet
@wallet_bp.route('/init', methods=['POST'])
def init_wallet():
    # Validate the request data
    # Call init_wallet service
    # Serialize the response data.
    # Return response in json.
    try:
        data = WalletRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    wallet, error = wallet_services.init_wallet(data['user_id'], data['currency'])
    if error:
        return jsonify({"error": error}), 400

    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Wallet created successfully", "data": response}), 201

# Add money to wallet
@wallet_bp.route('/add_money', methods=['POST'])
def add_money():
    try:
        data = AddMoneyRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    wallet, error = wallet_services.add_money_to_wallet(data['user_id'], data['amount'])
    if error:
        return jsonify({"error": error}), 400

    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Money added to wallet", "data": response}), 200

# Hold money from wallet
@wallet_bp.route('/hold_money', methods=['POST'])
def hold_money():
    try:
        data = HoldRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    hold, error = wallet_services.hold_money(data['user_id'], data['amount'])
    if error:
        return jsonify({"error": error}), 400

    response = HoldResponseSchema().dump(hold)
    return jsonify({"message": "Money held successfully", "data": response}), 200

# Release hold money
@wallet_bp.route('/release_hold', methods=['POST'])
def release_hold():
    try:
        released_count = wallet_services.release_hold()
        if released_count == 0:
            return jsonify({"message": "No holds to release"}), 200
        return jsonify({"message": f"{released_count} holds released"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Reverse hold money
@wallet_bp.route('/reverse_hold', methods=['POST'])
def reverse_hold():
    try:
        data = ReverseHoldRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400
    
    hold, error = wallet_services.reverse_hold(data['user_id'], data['hold_id'])
    if error:
        return jsonify({"error": error}), 400
    
    response = HoldResponseSchema().dump(hold)
    return jsonify({"message": "Hold reversed successfully", "data": response}), 200