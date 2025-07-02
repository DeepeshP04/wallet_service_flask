from flask import Flask
from extensions import db

# Create app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'
db.init_app(app)

# Create tables
with app.app_context():
    print("Creating tables...")
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)