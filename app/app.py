from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .settings import DATABASE_NAME
from .endpoints import user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/{}'.format(DATABASE_NAME)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(user)
