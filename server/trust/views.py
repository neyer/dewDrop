from django.shortcuts import render

from drops.models import Address
from drops.models import Network
from drops.models import Statement

from drops.views import _json_response


def statements_by_user(request, author_network, author_name):

    by_subject = {}

    for s in Statement.objects.filter(author__network__name=author_network,
                                      author__name=author_name,
                                      content__endswith='trust').\
                                      order_by('-timestamp'):

        if not s.subject.id in by_subject:
            record = s.subject.to_json()
            record['trust'] = s.content == 'trust'
            by_subject[s.subject.id] = record
    return _json_response(by_subject)
        







