from flask import Flask
from app.extensions import db, migrate
from app.models import Wallet, Hold, OperationLog

def create_app():
    # Create app and configure database
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'
    db.init_app(app)
    migrate.init_app(app, db)

    # Create tables
    with app.app_context():
        db.create_all()
        print("Tables created successfully")

    # Register blueprints
    from app.routes.wallet_routes import wallet_bp
    from app.routes.report_routes import report_bp
    app.register_blueprint(wallet_bp)
    app.register_blueprint(report_bp)

    return app