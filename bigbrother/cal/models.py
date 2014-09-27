__author__ = 'yenda'

from django.db import models
from django.conf import settings

from institution.models import Membership, Classroom
from lectures.models import Lecture


class Event(models.Model):
    lecture = models.ForeignKey(Lecture, related_name="events")
    type = models.CharField(max_length=50)
    adeweb_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    classrooms = models.ManyToManyField(Classroom, related_name="events")
    memberships = models.ManyToManyField(Membership, related_name="events")
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events")
    report = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.start, self.lecture.name)
