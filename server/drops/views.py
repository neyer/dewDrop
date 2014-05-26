from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from drops.models import Address
from drops.models import Network
from drops.models import Statement

import json
import logging
import time

logger = logging.getLogger(__name__)

def _json_response(js):
    return HttpResponse(json.dumps(js),
                        content_type='application/json')


def _validate_json(body, expected):
    missing = []

    for key in expected:
        if not key in body:
            missing.append(key)

    if missing: 
        return False, { 'missing' : missing }
    else:
        return True, {}

def index(request):
    return HttpResponse(':)')


@csrf_exempt
def make_statement(request):

    # first get the body to make sure this guy is valid
    body = json.loads(request.body)

    expected = [ 'author_name', 'author_network', 
                 'subject_name', 'subject_network' ]

    valid, errors = _validate_json(body, expected)
    if not valid:
        return _json_response({'success' : False,
                                'errors' : errors })
                                            
    # extract the fields from the body 
    # create the appropriate networks/addresses if needed

    subj_network_name = body['author_network']
    auth_network_name = body['subject_network']
    auth_name = body['author_name']
    subj_name = body['subject_name']
    content = body['content']
    
    a_network, created = Network.objects.get_or_create(name=auth_network_name)
    if created: a_network.save()

    author, created = Address.objects.get_or_create(network=a_network,
                                                    name=auth_name)
    if created: author.save()

    s_network, created = Network.objects.get_or_create(name=subj_network_name)
    if created: s_network.save()

    subject, created = Address.objects.get_or_create(name=subj_name,
                                                     network=s_network)
    if created: subject.save()

    s = Statement.create(author, content, subject)
    s.save()

    return _json_response({'success' : True,
                           'id' : s.id})

def check_statement(request,
                    author_network, author_name,
                    content,
                    subject_network, subject_name):


    for s in Statement.objects.filter(author__network__name=author_network,
                                author__name=author_name,
                                content=content,
                                subject__network__name=subject_network,
                                subject__name=subject_name).\
                                order_by('-timestamp'):
        return _json_response({ 'exists' : True,
                                'timestamp'  : s.timestamp})
    return _json_response({ 'exists' : False })
