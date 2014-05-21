from django.db import models

class Network(models.Model):
    """Social network (Facebook, Twitter, G+) or category of 
    identity provider (email) """
    name = models.CharField(max_length=256)


class Address(models.Model):
    """An Address is a vertex on a social Network. The `address` of the vertex
    is used to uniqueify it in that network.
    
    For example, a phone number is an address on the phone network.
    the 'name' of that adderss is the same as the phone number. 
    The network is 'telephone.'"""
    name = models.CharField(max_length=1024,default="")
    network = models.ForeignKey(Network)


class Statement(models.Model):
    author = models.ForeignKey(Address,
                                related_name='statements_made')
    subject = models.ForeignKey(Address, 
                                blank=True,
                                related_name="statements_about") 
    content = models.TextField(default="") 
    timestamp = models.FloatField()


