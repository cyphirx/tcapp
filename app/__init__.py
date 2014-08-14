from flask import Flask
from flask.ext.login import LoginManager
app = Flask(__name__)

app.secret_key = "Some key used for creating hidden tags"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cache.db'

lm = LoginManager()
lm.init_app(app)

from models import db
db.init_app(app)

from app import views


