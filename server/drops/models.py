from django.contrib import admin
from django.db import models

import json
import time

class Network(models.Model):
    """Social network (Facebook, Twitter, G+) or category of 
    identity provider (email) """
    name = models.CharField(max_length=256)

    def __str__(self):
        return 'Network {}'.format(self.name)

    class Admin(admin.ModelAdmin):
        pass

admin.site.register(Network, Network.Admin)


class Address(models.Model):
    """An Address is a vertex on a social Network. The `address` of the vertex
    is used to uniqueify it in that network.
    
    For example, a phone number is an address on the phone network.
    the 'name' of that adderss is the same as the phone number. 
    The network is 'telephone.'"""
    name = models.CharField(max_length=1024,default="")
    network = models.ForeignKey(Network)

    def __str__(self):
        return '{}.{}'.format(self.network.name, self.name)

    def to_json(self):
        return { 'network' : self.network.name,
                 'name' : self.name }

    class Meta:
        verbose_name_plural = 'Addresses'

    class Admin(admin.ModelAdmin):
        pass

admin.site.register(Address, Address.Admin)

def _validate_json(body, expected):
    missing = []

    for key in expected:
        if not key in body:
            missing.append(key)
    if missing: 
        return False, { 'missing' : missing }
    else:
        return True, {}


class Statement(models.Model):
    """
        The meat of the system here. Statements can have the following category

        trust/distrust:
            takes a url

            reflects the content of the subject which made the referred statment
                trust an article you think represents a genuine opinion

            distrust a url you think does not reflect the opinion of the subject
                i.e. a  url that you feel is not genuine

        agree/disagree: reflects the content of the referred statement only
            takes a url

            agree with a statement that you also feel comfortable making

            disagree with a statement that you feel comfortable negating

            i can create transitive trust by saying "i agree with any statement avishaan makes of the form, i trust X"

        same-as: reflects a belief that two authors are the same
            takes two addresses.
            the urls can be identities:
               - i say these two addresses belong to the same person

        offend: reflects a belief that address 1 has offended address 2
            takes two addresses
    
        forgive: reflects a belief that address 1 has forgiven an offensive
            takes one address, one url
              
    """
    author = models.ForeignKey(Address,
                                related_name='statements')
    subject_1 = models.URLField(max_length=1024)
    subject_2 = models.URLField(max_length=1024)
    
    # statements fit into these categories,
    PossibleCategories = ['TRUST',
                          'DISTRUST',
                          'AGREE',
                          'DISAGREE',
                          'SAME-ADDRESS',
                          'OFFEND',
                          'FORGIVE']
    CategoryChoices = [ (c,c) for c in PossibleCategories]
    
    category = models.CharField(max_length=16,choices=CategoryChoices,default='TRUST')
    # the comment contains details and more involved information
    comment = models.TextField(default="")
    # when the statement happened
    timestamp = models.FloatField()

    def __str__(self):
        return "at {} {} says {} {} {}".format(self.timestamp,
                                            self.author,
                                            self.category,
                                            self.subject_1,
                                            self.subject_2 or "")
    @classmethod
    def make_trust_statement(classs, body):
        valid, errors = _validate_json(body, expected)
        if not valid:
            return errors

        author_network = body['author_network']
        author_name = body['author_network']
        a_network, created = Network.objects.get_or_create(name=author_network)
        if created: a_network.save()

        author, created = Address.objects.get_or_create(network=a_network,
                                                        name=author_name)
        if created: author.save()

        # we'll need some validation to verify each statement source
        # in the future, dewdrop users (ones making statements) 
        # will be able to make statements about which email address/twitter
        # /fb account they own, and dewdrop can agree that these are valid



         

admin.site.register(Statement)
