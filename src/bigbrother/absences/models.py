__author__ = 'yenda'
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from ..calendar.models import Event


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