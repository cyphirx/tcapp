from pprint import pprint
from app.api import api
import json
import urllib2


@api.route('/')
def show():
    ''' JSON function to report all publicly available api calls '''
    pass

@api.route('/check/incursion')
def check_incursions():
    # Three states
    #  - Established
    #  - Mobilizing
    #  - Withdrawing
    # Max runtime for an incursion
    MAX_TIME = 6
    # Build request and add User-agent string
    #req = urllib2.Request(url='http://public-crest.eveonline.com/incursions/')
    #req.add_header('User-agent', 'TCApp - http://github.com/cyphirx/tcapp')
    #response = urllib2.urlopen(req)
    response = open('incursion_sample.txt')
    incursions = json.load(response)
    for item in incursions['items']:
        #pprint(item)
        print item['state']


    # Clean up any remaining incursions
    return ''