__author__ = 'yenda'

from django.contrib import admin
from .models import Lecture, Teacher

admin.site.register(Lecture)
admin.site.register(Teacher)