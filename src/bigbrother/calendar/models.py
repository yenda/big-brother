__author__ = 'yenda'
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ..institution.models import Membership, Classroom


class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = _(u'activities')

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Event(models.Model):
    activity = models.ForeignKey(Activity, related_name="events")
    adeweb_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    classrooms = models.ManyToManyField(Classroom, related_name="events")
    memberships = models.ManyToManyField(Membership, related_name="events")
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.start, self.activity.name)
