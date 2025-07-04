from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create SQLAlchemy and migrate instance
db = SQLAlchemy()
migrate = Migrate()