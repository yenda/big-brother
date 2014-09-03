__author__ = 'yenda'

#TODO this file should be documented


import xml.sax

from django.contrib.auth import get_user_model
from datetime import datetime

from ..calendar.models import Activity, Event
from ..institution.models import Membership, Classroom


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
                self.student, created = get_user_model().objects.get_or_create(username=self.name, adeweb_id=self.adeweb_id, category="student")
            elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
                self.student = None
                name = attrs.getValue('name')
                adeweb_id = attrs.getValue('id')
                get_user_model().objects.get_or_create(username=name, adeweb_id=adeweb_id, category="instructor")
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
            time = datetime.strptime(attrs.getValue("startHour"), "%H:%M")
            start = date.replace(hour=time.hour, minute=time.minute, second=0)
            time = datetime.strptime(attrs.getValue("endHour"), "%H:%M")
            end = date.replace(hour=time.hour, minute=time.minute, second=0)
            adeweb_id = attrs.getValue("id")
            self.event, created = Event.objects.get_or_create(activity=self.activity,
                                                              adeweb_id=adeweb_id,
                                                              start=start,
                                                              end=end)

        elif name == "eventParticipant":
            if attrs.getValue('category') == "classroom":
                classroom, created = Classroom.objects.get_or_create(name=attrs.getValue('name'))
                self.event.classrooms.add(classroom)
            elif attrs.getValue('category') == "instructor":
                teacher, created = get_user_model().objects.get_or_create(username=attrs.getValue('name'),
                                                                          adeweb_id=attrs.getValue('id'),
                                                                          category="instructor")
                self.event.teachers.add(teacher)
            elif attrs.getValue('category') == "trainee":
                group, created = Membership.objects.get_or_create(name=attrs.getValue('name'),
                                                                  adeweb_id=attrs.getValue('id'))
                self.event.groups.add(group)