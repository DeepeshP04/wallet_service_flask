from flask import Blueprint, jsonify, request
from wallet_schema import WalletBalanceRequestSchema, WalletResponseSchema
from services import wallet_services, report_services

report_bp = Blueprint('report', __name__, url_prefix='/report')

@report_bp.route('/wallet_balance', methods=['GET'])
def wallet_balance():
    try:
        data = WalletBalanceRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    wallet, error = report_services.get_wallet_balance(data['user_id'])
    if error:
        return jsonify({"error": error}), 404

    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Wallet balance fetched successfully", "data": response}), 200