from flask import Flask
from extensions import db
from flask_migrate import Migrate

def create_app():
    # Create app and configure database
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'
    db.init_app(app)
    migrate = Migrate(app, db)

    # Create tables
    with app.app_context():
        db.create_all()
        print("Tables created successfully")

    # Register blueprints
    from wallet_routes import wallet_bp
    app.register_blueprint(wallet_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)