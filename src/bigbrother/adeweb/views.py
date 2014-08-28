__author__ = 'yenda'

#TODO :This file should contain real views with a form to only validate the action once the password of the user is entered otherwise this will lead to problems in the future

from .backends.api import load_api
from .parser import SaxParsingActivities, SaxParsingResources
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from ..models import (Student, Activity, Teacher, Group, Classroom, Event, Absence)

import xml


def update_resources(self):
    api = load_api()
    api.connect()
    api.set_project()
    resources = api.get_resources()
    xml.sax.parseString(resources, SaxParsingResources())
    api.disconnect()
    return redirect(reverse('admin:index'))


def write_resources(self):
    api = load_api()
    resources = api.get_resources()
    with open("resources.xml", 'w') as f:
        f.write(resources)


def update_activities(self):
    api = load_api()
    api.connect()
    api.set_project()
    activities = api.get_activities()
    with open("activities.xml", 'w') as f:
        f.write(activities)
    #xml.sax.parseString(activities, SaxParsingActivities())
    api.disconnect()
    return redirect(reverse('admin:index'))


def delete_all(cls):
    query_set = cls.objects.only("pk")  # No ordering, pull the least info possible.
    for item in query_set:
        item.delete()


def delete_data(self):
    delete_all(Group)
    delete_all(Classroom)
    delete_all(Event)
    delete_all(Teacher)
    delete_all(Activity)
    delete_all(Absence)
    delete_all(Student)
    return redirect(reverse('admin:index'))