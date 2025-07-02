from flask import Blueprint, jsonify, request
from wallet_schema import WalletResponseSchema, AddMoneyRequestSchema
import services

wallet_bp = Blueprint('wallet', __name__, url_prefix='/wallet')

# Initialize wallet
@wallet_bp.route('/init', methods=['POST'])
def init_wallet():
    wallet = services.init_wallet()
    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Wallet created successfully", "data": response}), 201

@wallet_bp.route('/add_money', methods=['POST'])
def add_money():
    try:
        data = AddMoneyRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    wallet, error = services.add_money_to_wallet(data['wallet_id'], data['amount'])
    if error:
        return jsonify({"error": error}), 400

    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Money added to wallet", "data": response}), 200
