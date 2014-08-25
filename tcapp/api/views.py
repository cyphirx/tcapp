from tcapp.models import db, User

from tcapp.api import api

@api.route('/')
def api_route():
    users = User.query.all()
    for user in users:
        print user.firstname
    return "API Return"
