from app import app
import os
from app.forms import LoginForm

from models import db, Account, Player, initial_db
from flask import render_template, Markup, session, redirect, url_for, request, jsonify, abort, flash
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

initial_db()

# Read in Configuration variables
apiURL = ConfigSectionMap("general")['apiurl']
debug = ConfigSectionMap("general")['debug']
interface = ConfigSectionMap("general")['interface']
port = int(os.environ.get("PORT", 5000))
localAPI = ConfigSectionMap("general")['localapi']

# stopgap until we can get connected to Auth
user = ConfigSectionMap("users")['user']
password = ConfigSectionMap("users")['password']

@app.route('/index')
@app.route('/')
def default_display():
    return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Username="' + form.name.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)



    # vim: set ts=4 sw=4 et :