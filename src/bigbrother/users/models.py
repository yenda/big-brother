__author__ = 'yenda'
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    name = models.CharField(max_length=100)
    adeweb_id = models.IntegerField()
    mail = models.CharField(max_length=100, default="yenda1@gmail.com")
    category = models.CharField(max_length=100, default="student")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name
