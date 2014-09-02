__author__ = 'yenda'
from django.db import models
from django.utils.translation import ugettext_lazy as _
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
    groups = models.ManyToManyField(Membership, related_name="events")
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" % (self.start, self.activity.name)


class Absence(models.Model):
    event = models.ForeignKey(Event, related_name="absences")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="absences")
    excuse = models.TextField(blank=True)

    @property
    def excused(self):
        if self.excuse == "":
            return False
        return True


class AbsenceReport(models.Model):
    code = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="absence_report")
    event = models.ForeignKey(Event, related_name="absence_reports")
    validated = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/report/%i/" % self.id