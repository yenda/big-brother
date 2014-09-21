__author__ = 'yenda'
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    adeweb_id = models.CharField(max_length=20, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.username

    def image_url(self):
        return "bigbrother/img/trombi/{0}-{1}.jpg".format(self.last_name.lower(), self.first_name.lower())

    def is_instructor(self):
        return self.groups.filter(name="instructor").exists()