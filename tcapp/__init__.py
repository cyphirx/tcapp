from flask import Flask

app = Flask(__name__)

app.secret_key = 'development key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tcapp:somepassword@zeus/tcapp'

from tcapp.api import api

from models import db
db.init_app(app)

app.register_blueprint(api, url_prefix='/api')

import tcapp.views