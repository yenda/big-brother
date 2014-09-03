__author__ = 'yenda'

from django.contrib import admin
from .models import Absence, AbsenceReport

admin.site.register(AbsenceReport)
admin.site.register(Absence)