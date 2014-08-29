__author__ = 'yenda'
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    adeweb_id = models.IntegerField()
    mail = models.CharField(max_length=100, default="yenda1@gmail.com")

    class Meta:
        abstract = True


class Student(Profile):

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Teacher(Profile):

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="groups")


class Classroom(models.Model):
    name = models.CharField(max_length=100)


class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Event(models.Model):
    activity = models.ForeignKey(Activity, related_name="events")
    adeweb_id = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    classrooms = models.ManyToManyField(Classroom, related_name="events")
    groups = models.ManyToManyField(Group, related_name="events")
    teachers = models.ManyToManyField(Teacher, related_name="events")


class Absence(models.Model):
    activity = models.ForeignKey(Activity, related_name="absences")
    student = models.ForeignKey(Student, related_name="absences")
    excuse = models.TextField(blank=True)

    @property
    def excused(self):
        if self.excuse == "":
            return False
        return True


class AbsenceReport(models.Model):
    code = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="absence_report")
    activity = models.ForeignKey(Activity, related_name="absence_reports")