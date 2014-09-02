__author__ = 'yenda'

from django.contrib import admin
from .models import (Membership, Classroom, Activity, Absence, AbsenceReport, Event)

admin.site.register(Event)
admin.site.register(Membership)
admin.site.register(Classroom)
admin.site.register(Activity)
admin.site.register(Absence)
admin.site.register(AbsenceReport)