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
        self.adeweb_id = None

    def startElement(self, name, attrs):
        if name == "resource":
            category = attrs.getValue('category')
            is_group = attrs.getValue('isGroup')
            if attrs.getValue('category') and category == 'category5' and is_group == "false":
                self.name = attrs.getValue('name')
                self.adeweb_id = attrs.getValue('id')
                self.student = Student(name=self.name, adeweb_id=self.adeweb_id)
                self.student.save()
            elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
                self.student = None
                name = attrs.getValue('name')
                adeweb_id = attrs.getValue('id')
                teacher = Teacher(name=name, adeweb_id=adeweb_id)
                teacher.save()
        elif name == "membership":
            if self.student:
                group, created = Group.objects.get_or_create(name=attrs.getValue('name'))
                group.students.add(self.student)

    def endElement(self, name):
        pass


class SaxParsingActivities(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.nameActivity=None
        self.type = None
        self.activity = None
        self.event = None

    def startElement(self, name, attrs):
        if name == "activity":
            self.nameActivity = attrs.getValue('name')
            self.type = attrs.getValue('type')
            self.activity, created = Activity.objects.get_or_create(name=self.nameActivity, type=self.type)

        elif name == "event":
            date = datetime.strptime(attrs.getValue("date"), "%d/%m/%Y")
            start_time = datetime.strptime(attrs.getValue("startHour"), "%H:%M")
            end_time = datetime.strptime(attrs.getValue("endHour"), "%H:%M")
            adeweb_id = attrs.getValue("id")
            self.event = Event(activity=self.activity,
                               adeweb_id=adeweb_id,
                               date=date,
                               start_time=start_time,
                               end_time=end_time)
            self.event.save()

        elif name == "eventParticipant":
            if attrs.getValue('category') == "classroom":
                classroom, created = Classroom.objects.get_or_create(name=attrs.getValue('name'))
                self.event.classrooms.add(classroom)
            elif attrs.getValue('category') == "instructor":
                try:
                    teacher = Teacher.objects.get(name=attrs.getValue("id"))
                    self.event.teachers.add(teacher)
                except ObjectDoesNotExist:
                    pass
            elif attrs.getValue('category') == "trainee":
                try:
                    group = Group.objects.get(name=attrs.getValue('name'))
                    self.event.groups.add(group)
                except ObjectDoesNotExist:
                    pass
            self.activity.save()