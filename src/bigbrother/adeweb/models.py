__author__ = 'yenda'

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


def user_factory(username, adeweb_id, email=None, group="student"):
    user = get_user_model().objects.filter(adeweb_id=adeweb_id)
    if user.exists():
        return user[0]
    else:
        username = username.title()
        last_name, first_name = username.split()
        username = '{0}.{1}'.format(first_name.lower(), last_name.lower())
        user = get_user_model().objects.create(username=username,
                                               first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               adeweb_id=adeweb_id)
        group = Group.objects.get(name=group)
        user.groups.add(group)
    return user


class Resource(models.Model):
    adeweb_id = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    isGroup = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField()
    creation = models.DateTimeField()
    father = models.ForeignKey("Resource")
    members = models.ForeignKey("Resource", related_name="memberships")