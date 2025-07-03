from flask import Blueprint, jsonify, request
from app.schemas.schema import WalletBalanceRequestSchema, WalletResponseSchema, HoldReportRequestSchema, HoldReportResponseSchema, WalletOperationRequestSchema, WalletOperationResponseSchema
from app.services import wallet_services, report_services

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

@report_bp.route('/hold_report', methods=['GET'])
def hold_report():
    try:
        data = HoldReportRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    result, error = report_services.get_hold_report(data['user_id'])
    if error:
        return jsonify({"error": error}), 404

    response = HoldReportResponseSchema().dump(result)
    return jsonify({"message": "Hold report fetched successfully", "data": response}), 200

@report_bp.route('/wallet_operation_report', methods=['GET'])
def wallet_operation_report():
    try:
        data = WalletOperationRequestSchema().load(request.get_json())
    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400

    result, error = report_services.get_wallet_operation_report(data['user_id'])
    if error:
        return jsonify({"error": error}), 404

    response = WalletOperationResponseSchema().dump(result)
    return jsonify({"message": "Wallet operation report fetched successfully", "data": response}), 200