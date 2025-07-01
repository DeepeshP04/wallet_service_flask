from flask_sqlalchemy import SQLAlchemy
from app import app

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'

# Create SQLAlchemy instance
db = SQLAlchemy(app)