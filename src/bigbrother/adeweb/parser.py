__author__ = 'yenda'

#TODO this file should be documented


import xml.sax

from datetime import datetime
from django.contrib.auth import get_user_model

from .models import user_factory
from ..calendar.models import Event
from ..institution.models import Membership, Classroom
from ..lecture.models import Lecture, Teacher


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
                email = attrs.getValue('email')
                self.student = user_factory(username=self.name, adeweb_id=self.adeweb_id, email=email)
            elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
                self.student = None
                name = attrs.getValue('name')
                adeweb_id = attrs.getValue('id')
                email = attrs.getValue('email')
                user_factory(username=name, adeweb_id=adeweb_id, email=email)
        elif name == "membership":
            if self.student:
                group, created = Membership.objects.get_or_create(name=attrs.getValue('name'),
                                                                  adeweb_id=attrs.getValue('id'))
                group.students.add(self.student)

    def endElement(self, name):
        pass


class SaxParsingActivities(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.lecture_name = None
        self.lecture = None
        self.type = None
        self.activity = None
        self.event = None

    def startElement(self, name, attrs):
        if name == "activity":
            self.lecture_name = attrs.getValue('name')
            self.type = attrs.getValue('type')
            self.lecture, created = Lecture.objects.get_or_create(name=self.lecture_name)

        elif name == "event":
            date = datetime.strptime(attrs.getValue("date"), "%d/%m/%Y")
            time = datetime.strptime(attrs.getValue("startHour"), "%H:%M")
            start = date.replace(hour=time.hour, minute=time.minute, second=0)
            time = datetime.strptime(attrs.getValue("endHour"), "%H:%M")
            end = date.replace(hour=time.hour, minute=time.minute, second=0)
            adeweb_id = attrs.getValue("id")
            self.event, created = Event.objects.get_or_create(lecture=self.lecture,
                                                              type=self.type,
                                                              adeweb_id=adeweb_id,
                                                              start=start,
                                                              end=end)

        elif name == "eventParticipant":
            if attrs.getValue('category') == "classroom":
                classroom, created = Classroom.objects.get_or_create(name=attrs.getValue('name'))
                self.event.classrooms.add(classroom)
            elif attrs.getValue('category') == "instructor":
                try:
                    adeweb_id = attrs.getValue('id')
                    teacher = get_user_model().objects.get(adeweb_id=adeweb_id)
                    self.event.teachers.add(teacher)
                    Teacher.objects.get_or_create(lecture=self.lecture, user=teacher)
                except get_user_model().DoesNotExist:
                    pass
            elif attrs.getValue('category') == "trainee":
                membership, created = Membership.objects.get_or_create(name=attrs.getValue('name'),
                                                                       adeweb_id=attrs.getValue('id'))
                self.event.memberships.add(membership)