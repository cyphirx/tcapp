from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from app.api import api
from app.srp import srp


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(api, url_prefix = '/api')
app.register_blueprint(srp, url_prefix = '/srp')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db.init_app(app)

from app import views, models