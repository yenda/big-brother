__author__ = 'yenda'

from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Activity


def groups(instance):
    return ', '.join(instance.groups)


class ActivityAdmin(admin.ModelAdmin):
    fields = ['name', 'activity_id', 'type', 'date', 'start_time', 'end_time', 'groups', 'teachers', 'classroom']


class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'student_id', 'groups']


class TeacherAdmin(admin.ModelAdmin):
    fields = ['name', 'teacher_id']

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Activity, ActivityAdmin)