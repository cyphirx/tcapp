from app.srp import srp
from flask import redirect

@srp.route('/')
@srp.route('/index')
def show_default():
    return "This page will eventually be here"

# Pretty bad hack due to lack of blueprint support in url_for
@srp.route('/<page>')
def redirect_routes(page):
    return redirect("srp/index")