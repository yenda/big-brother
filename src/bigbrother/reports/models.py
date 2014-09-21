__author__ = 'yenda'
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from ..calendar.models import Event
from datetime import datetime


class Absence(models.Model):
    event = models.ForeignKey(Event, related_name="absences")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="absences")
    excuse = models.TextField(blank=True)

    @property
    def excused(self):
        if self.excuse == "":
            return False
        return True