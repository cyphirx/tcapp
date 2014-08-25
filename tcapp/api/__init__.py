from flask import Blueprint

api = Blueprint('api', __name__)

from tcapp.api import views