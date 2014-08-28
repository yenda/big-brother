__author__ = 'yenda'

#TODO this file should be documented

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from ..models import (Student, Activity, Teacher, Group, Classroom, Event)

import xml.sax
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class SaxParsingResources(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.name = None
        self.groups = None
        self.student = None
        self.student_id = None

    def startElement(self, name, attrs):
        if name == "resource":
            if attrs.getValue('category') and attrs.getValue('category') == 'category5':
                self.name = attrs.getValue('name')
                self.student_id = attrs.getValue('id')
                self.student = Student(name=self.name, adeweb_id=self.student_id)
                self.student.save()
            elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
                self.student = None
                name = attrs.getValue('name')
                teacher_id = attrs.getValue('id')
                teacher = Teacher(name=name, adeweb_id=teacher_id)
                teacher.save()
        elif name == "membership":
            if self.student:
                try:
                    group = Group.objects.get(name=attrs.getValue('name'))
                except ObjectDoesNotExist:
                    group = Group(name=attrs.getValue('name'))
                    group.save()
                self.student.groups.add(group)
                self.student.save()

    def endElement(self, name):
        pass


class SaxParsingActivities(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.nameActivity=None
        self.type = None
        self.activity = None

    def startElement(self, name, attrs):
        if name == "activity":
            self.nameActivity = attrs.getValue('name')
            self.type = attrs.getValue('type')
            self.activity = None

        elif name == "event":
            date = datetime.strptime(attrs.getValue("date"), "%d/%m/%Y")
            start_time = datetime.strptime(attrs.getValue("startHour"), "%H:%M")
            end_time = datetime.strptime(attrs.getValue("endHour"), "%H:%M")
            activity_id = attrs.getValue("id")
            self.activity = Activity(name=self.nameActivity,
                                     activity_id=activity_id,
                                     type=self.type,
                                     date=date,
                                     start_time=start_time,
                                     end_time=end_time)
            self.activity.save()

        elif name == "eventParticipant":
            if attrs.getValue('category') == "classroom":
                try:
                    classroom = Classroom.objects.get(name=attrs.getValue('name'))
                except ObjectDoesNotExist:
                    classroom = Classroom(name=attrs.getValue('name'))
                    classroom.save()
                self.activity.classrooms.add(classroom)
            elif attrs.getValue('category') == "instructor":
                try:
                    teacher = Teacher.objects.get(name=attrs.getValue("id"))
                    self.activity.teachers.add(teacher)
                except ObjectDoesNotExist:
                    pass
            elif attrs.getValue('category') == "trainee":
                try:
                    group = Group.objects.get(name=attrs.getValue('name'))
                    self.activity.groups.add(group)
                except ObjectDoesNotExist:
                    pass
            self.activity.save()