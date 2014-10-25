from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from drops.models import Address
from drops.models import Network
from drops.models import Statement
from drops.models import _validate_json

import json
import logging
import time

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse(':)')


@csrf_exempt
def make_statement(request):

    # first get the body to make sure this guy is valid
    body = json.loads(request.body)

    expected = [ 'category' ]

    valid, errors = _validate_json(body, expected)
    if not valid:
        return JsonResponse({'success' : False,
                                'errors' : errors })
                                            
    # extract the fields from the body 
    # create the appropriate networks/addresses if needed

    category = body['category']
    subj_network_name = body['author_network']
    auth_name = body['author_name']
    
    s_network, created = Network.objects.get_or_create(name=subj_network_name)
    if created: s_network.save()

    subject, created = Address.objects.get_or_create(name=subj_name,
                                                     network=s_network)
    if created: subject.save()

    s = Statement.create(author, content, subject)
    s.save()

    return JsonResponse({'success' : True,
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
        return JsonResponse({ 'exists' : True,
                                'timestamp'  : s.timestamp})
    return JsonResponse({ 'exists' : False })


def stating_addresses(request, content, subject_network, subject_name):
    by_network = {}
    last_maker = None
    for s in Statement.objects.filter(subject__network__name=subject_network,
                                      subject__name=subject_name,
                                      content=content).\
                                      order_by('timestamp', 'author'):
        if last_maker is None or (s.author.id != last_maker.id):
            auth_network = s.author.network.name
            auth_name = s.author.name
            authors = by_network.setdefault(auth_network,[])
            authors.append([s.timestamp,auth_name])
        last_maker = s.author

    return JsonResponse({'authors' : by_network})
            



