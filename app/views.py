from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
import os
from forms import LoginForm
from hashlib import sha1

from models import db, Account, Player
from ConfigParser import ConfigParser


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


Config = ConfigParser()
Config.read("settings.ini")

# Read in Configuration variables
apiURL = ConfigSectionMap("general")['apiurl']
debug = ConfigSectionMap("general")['debug']
interface = ConfigSectionMap("general")['interface']
port = int(os.environ.get("PORT", 5000))
localAPI = ConfigSectionMap("general")['localapi']
authAPI = ConfigSectionMap("general")['authapi']

# stopgap until we can get connected to Auth
user = ConfigSectionMap("users")['user']
password = ConfigSectionMap("users")['password']

@app.route('/index')
@app.route('/')
@login_required
def index():
    user = g.user
    return render_template('index.html',
                           title = 'Home',
                           user = user )


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Generate sha1 hash for TEST lookup
        m = sha1()
        m.update(form.password.data)
        hashed_pass = m.hexdigest()
        form.password.data = ""

        # Start lookup in auth

        flash('Login requested for OpenID="' + form.name.data + '", remember_me=' + str(form.remember_me.data) + ', pass hash=' + str(hashed_pass))

        session['remember_me'] = form.remember_me.data
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return Account.query.get(int(id))

    # vim: set ts=4 sw=4 et :