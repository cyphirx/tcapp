import urllib2
import json
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

groupID = int(ConfigSectionMap("groups")['groupid'])
adminID = int(ConfigSectionMap("groups")['adminid'])

# stopgap until we can get connected to Auth
user = ConfigSectionMap("users")['user']
password = ConfigSectionMap("users")['password']


@app.route('/index')
@app.route('/')
@login_required
def index():
    user = g.user
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
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
        # Leaving HTTP lookups for now until features are complete enough to hit it one-time only
        # authURL = authAPI + "/api/1.0/login/?user=" + form.name.data + "&pass=" + hashed_pass
        #try:
        #    f = urllib2.urlopen(authURL)
        #except:
        #    print authURL
        #    return "Error retrieving auth response"
        f = open('auth_sample.txt')

        data = json.load(f)

        # Verify auth was successful
        if data['auth'] != "ok":
            flash("Authentication error, please check username and password and try again.")
            return render_template('login.html', title='Sign In', form=form)

        # Check for group membership
        member = False
        for group in data['groups']:
            if int(group['id']) == groupID:
                member = True
            if int(group['id']) == adminID:
                admin = True
                session['admin'] = True

        if member == False:
            flash('Please apply to authgroup!')
            return render_template('login.html', title='Sign In', form=form)

        id = data['id']

        # Check if account/player exists and create if not
        if not db.session.query(Account).filter(Account.id == data['id']).scalar():
            # Retrieve account values
            username = data['username']
            primary_id = data['primarycharacter']['id']
            account = Account(id=id, username=username, primary_character=primary_id)
            db.session.add(account)

            # Retrieve player values
            primary_character = data['primarycharacter']
            characterName = primary_character['name']
            corporationID = primary_character['corporation']['id']
            corporationName = primary_character['corporation']['name']
            allianceID = False
            allianceName = False
            if primary_character['alliance']:
                if primary_character['alliance']['id']:
                    allianceID = primary_character['alliance']['id']
                    allianceName = primary_character['alliance']['name']
            player = Player(characterID=primary_id, characterName=characterName, corporationID=corporationID,
                            corporationName=corporationName, allianceID=allianceID, allianceName=allianceName)
            db.session.add(player)
            db.session.commit()
        else:
            print "loading user"
            account = Account.query.get(id)

            login_user(account, remember=form.remember_me.data)
            # Update access time and carry on
            return redirect(request.args.get('next') or url_for('index'))
            pass

        session['remember_me'] = form.remember_me.data
        return redirect('/index')

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@lm.user_loader
def load_user(id):
    account = Account.query.get(id)
    return account

    # vim: set ts=4 sw=4 et :