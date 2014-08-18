from pprint import pprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app
from app.api import api

import json
import urllib2
from app.models import Incursion, Account

db = current_app.db
@api.route('/')
def show():
    ''' JSON function to report all publicly available api calls '''
    return "Hi"


@api.route('/check/incursion')
def check_incursions():
    # Three states
    #  - Established
    #  - Mobilizing
    #  - Withdrawing
    # Max runtime for an incursion
    MAX_TIME = 7
    # Build request and add User-agent string
    #req = urllib2.Request(url='http://public-crest.eveonline.com/incursions/')
    #req.add_header('User-agent', 'TCApp - http://github.com/cyphirx/tcapp')
    #response = urllib2.urlopen(req)
    response = open('incursion_sample.txt')
    incursions = json.load(response)
    constellation = []
    for item in incursions['items']:
        pprint(item)
        print item['state']
        constellation.append(item['constellation']['id_str'])
        sites = db.session.query(Incursion).filter()
        #incursion = Incursion(constellation=int(item['constellation']), staging=int(item['stagingSolarSystem']['id']))
       # db.session.add(incursion)
       # db.session.commit()
        accounts = db.session.query(Account).all()
        for account in accounts:
            print account.username

    print str(int(constellation[2]))
    # Clean up any remaining incursions
    return ''