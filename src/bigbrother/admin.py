__author__ = 'yenda'

from django.contrib import admin
from .models import (Student, Teacher, Group, Classroom, Activity, Absence, AbsenceReport)


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Classroom)
admin.site.register(Activity)
admin.site.register(Absence)
admin.site.register(AbsenceReport)