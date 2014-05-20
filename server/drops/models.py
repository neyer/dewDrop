from django.db import models

class Network(models.Model):
    """Social network (Facebook, Twitter, G+) or category of 
    identity provider (email) """
    name = models.CharField(max_length=256)

class Identity(models.Model):
    # email address, facebook id, phone number, etc
    # so for an email identity, the network is 'email', the email address 
    # for a phone identity, network is 'phone' and the 'address' is 
    # the phone number
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


