__author__ = 'yenda'
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    adeweb_id = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=100, default="student")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.username

    def is_instructor(self):
        return self.category=="instructor"