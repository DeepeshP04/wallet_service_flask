from flask import Blueprint
from app import app
from services import init_wallet

wallet_bp = Blueprint('wallet', __name__, url_prefix='/wallet')

# Initialize wallet
@app.route('/init', methods=['POST'])
def init_wallet():
    
    
