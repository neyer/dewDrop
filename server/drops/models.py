from django.db import models

class Network(models.Model):
    """Social network (Facebook, Twitter, G+) or category of 
    identity provider (email) """
    name = models.CharField(max_length=256)


class Identity(models.Model):
    """An Identity is a vertex on a social Network. The `address` of the vertex is used to uniqueify it in that network. For example, a phone number is an identity on the phone network. the 'address' of that identity is the same as the phone number.  The network is 'telephone.'"""
    address = models.CharField(max_length=1024,default="")
    network = models.ForeignKey(Network)


class Statement(models.Model):
    author = models.ForeignKey(Identity,
                                related_name='statements_made')
    subject = models.ForeignKey(Identity, 
                                blank=True,
                                related_name="statements_about") 
    content = models.TextField(default="") 
    timestamp = models.FloatField()


