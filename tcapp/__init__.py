from flask import Flask

app = Flask(__name__)
import config

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI

from tcapp.api import api


from models import db
db.init_app(app)

app.register_blueprint(api, url_prefix='/api')

import tcapp.views