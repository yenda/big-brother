__author__ = 'yenda'

#TODO :This file should contain real views with a form to only validate the action once the password of the user is entered otherwise this will lead to problems in the future

from .backends.api import load_api
from .parser import SaxParsingActivities, SaxParsingResources
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

import xml
import os

from absences.models import Absence
from cal.models import Event
from lectures.models import Lecture
from institution.models import Classroom, Membership


@staff_member_required
def update_resources(self):
    api = load_api()
    api.connect()
    api.set_project()
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../activities.xml')
    with open(path, "r") as f:
        resources = f.read()
        resources = resources.encode('utf-8')
    xml.sax.parseString(resources, SaxParsingResources())
    api.disconnect()
    return redirect(reverse('admin:index'))


@staff_member_required
def write_resources(self):
    api = load_api()
    resources = api.get_resources()
    with open("resources.xml", 'w') as f:
        f.write(resources)


@staff_member_required
def update_activities(self):
    api = load_api()
    api.connect()
    api.set_project()
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../activities.xml')
    with open(path, "r") as f:
        activities = f.read()
        activities = activities.encode('utf-8')
        xml.sax.parseString(activities, SaxParsingActivities())
    api.disconnect()
    return redirect(reverse('admin:index'))


@staff_member_required
def write_activities(self):
    api = load_api()
    activities = api.get_activities()
    with open("activities.xml", 'w') as f:
        f.write(activities)


@staff_member_required
def delete_all(cls):
    query_set = cls.objects.only("pk")  # No ordering, pull the least info possible.
    for item in query_set:
        item.delete()


def delete_data(self):
    delete_all(Membership)
    delete_all(Classroom)
    delete_all(Event)
    delete_all(settings.AUTH_USER_MODEL)
    delete_all(Lecture)
    delete_all(Absence)
    return redirect(reverse('admin:index'))