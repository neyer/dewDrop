import json
import lazyopt
import requests
import time

AUTHOR_NAME='neyer'
SUBJECT_NAME='neyer'
AUTHOR_NETWORK='facebook'
SUBJECT_NETWORK='facebook'
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
    
    payload = { 'author_name': AUTHOR_NAME,
                'author_network':  AUTHOR_NETWORK,
                'subject_name':  SUBJECT_NETWORK,
                'subject_network':  SUBJECT_NETWORK,
                'content' : CONTENT }

    print 'payload is:\n', payload

    make_statement_url = '/make-statement'

    r = requests.post(SERVER_HOST+make_statement_url,
                      headers={'content-type':'application/json'},
                      data=json.dumps(payload))
    print '---\n',r.text, '---\n', r.headers
