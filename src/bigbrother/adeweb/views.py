__author__ = 'yenda'

#TODO :This file should contain real views with a form to only validate the action once the password of the user is entered otherwise this will lead to problems in the future

from .api import AdewebAPI
from .parser import SaxParsingActivities, SaxParsingResources
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from ..models import (Student, Activity, Teacher, Group, Classroom, Event, Absence)
import xml.sax


def update_resources(self):
    api = AdewebAPI()
    api.connect()
    api.set_project()
    resources = api.get_resources()
    with open("resources.xml", 'w') as f:
        f.write(resources)
    #xml.sax.parseString(resources, SaxParsingResources())
    api.disconnect()
    return redirect(reverse('admin:index'))


def update_activities(self):
    api = AdewebAPI()
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