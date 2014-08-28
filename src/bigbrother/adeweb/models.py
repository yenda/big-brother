__author__ = 'yenda'

from django.db import models


class Resource(models.Model):
    adeweb_id = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    isGroup = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField()
    creation = models.DateTimeField()
    father = models.ForeignKey("Resource")
    members = models.ForeignKey("Resource", related_name="memberships")