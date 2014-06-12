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



class Statement(models.Model):
    author = models.ForeignKey(Address,
                                related_name='statements_made')
    subject = models.ForeignKey(Address, 
                                blank=True,
                                related_name="statements_about") 
    content = models.TextField(default="") 
    timestamp = models.FloatField()

    def __str__(self):
        return "at {} {} says {} {}".format(self.timestamp,
                                            self.author,
                                            self.content,
                                            self.subject)

    @classmethod
    def create(classs, author, content, subject=None):
        s = Statement(author=author,
                      subject=subject,
                      content=content,
                      timestamp=time.time())
        return s


admin.site.register(Statement)
