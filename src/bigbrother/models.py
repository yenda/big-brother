__author__ = 'yenda'
from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    teacher_id = models.IntegerField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Group(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    groups = models.ManyToManyField(Group, related_name="students")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    activity_id = models.IntegerField()
    type = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    classrooms = models.ManyToManyField(Classroom, related_name="activities")
    groups = models.ManyToManyField(Group, related_name="activities")
    teachers = models.ManyToManyField(Teacher, related_name="activities")

    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s" % self.name


class Absence(models.Model):
    activity = models.ForeignKey(Activity, related_name="absences")
    student = models.ForeignKey(Student, related_name="absences")
    excuse = models.TextField(blank=True)

    @property
    def excused(self):
        if self.excuse == "":
            return False
        return True