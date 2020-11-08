from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from LibraryAPI import app, properties

app.config['SQLALCHEMY_DATABASE_URI'] = properties.DB_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
