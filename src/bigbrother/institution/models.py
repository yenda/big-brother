__author__ = 'yenda'
from django.db import models
from django.conf import settings


class Membership(models.Model):
    name = models.CharField(max_length=100)
    adeweb_id = models.IntegerField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="memberships")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name