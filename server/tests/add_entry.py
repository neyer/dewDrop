import json
import lazyopt
import requests
import time

AUTHOR_ID=1
SUBJECT_ID=1
CONTENT='trust'
SERVER_HOST = 'http://10.0.2.15:8000'
API_BASE_URL = '/api/v1'
ADDRESS_URL =  API_BASE_URL+'/address/'
NETWORK_URL =  API_BASE_URL+'/network/'
STATEMENT_URL = API_BASE_URL+'/statement/'
TIMESTAMP = time.time()

def make_address_url(address):
    return '{}{}/'.format(ADDRESS_URL,address)

if __name__ == '__main__':

    lazyopt.apply_all()
    
    payload = { 'author' : make_address_url(AUTHOR_ID),
                'subject' : make_address_url(SUBJECT_ID),
                'timestamp' : TIMESTAMP,
                'content' : CONTENT }

    print 'payload is:\n', payload



    r = requests.post(SERVER_HOST+STATEMENT_URL,
                      headers={'content-type':'application/json'},
                      data=json.dumps(payload))
    print '---\n',r.text, '---\n', r.headers
