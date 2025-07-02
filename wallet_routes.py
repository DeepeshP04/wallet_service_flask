from flask import Blueprint
from app import app
from services import init_wallet
from wallet_schema import WalletResponseSchema

wallet_bp = Blueprint('wallet', __name__, url_prefix='/wallet')

# Initialize wallet
@app.route('/init', methods=['POST'])
def init_wallet():
    wallet = init_wallet()
    response = WalletResponseSchema().dump(wallet)
    return jsonify({"message": "Wallet created successfully", "data": response})
    
