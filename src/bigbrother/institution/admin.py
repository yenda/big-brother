__author__ = 'yenda'

from django.contrib import admin
from .models import Membership, Classroom

admin.site.register(Membership)
admin.site.register(Classroom)