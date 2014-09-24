__author__ = 'yenda'
from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ..institution.models import Membership, Classroom


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Teacher")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lecture = models.ForeignKey(Lecture)
    position = models.CharField(max_length=100, blank=True)