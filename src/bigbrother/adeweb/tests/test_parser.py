__author__ = 'yenda'

from django.test.utils import override_settings
from django.test import TestCase
from django.test import Client

from ...models import (Student, Teacher, Classroom, Activity, Absence, AbsenceReport, Group, Event)
from ..views import update_resources, update_activities

@override_settings(ADEWEB_API={
    'BACKEND': 'bigbrother.adeweb.backends.dummy.API',
})
class ParsingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_resources(self):
        url = "/adeweb/updateResources"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, "User could not access the page %s" % url)
        update_resources(self)
        self.assertEqual(4, Student.objects.all().count())
        self.assertEqual(2, Teacher.objects.all().count())
        self.assertEqual(0, Classroom.objects.all().count())
        self.assertEqual(0, Activity.objects.all().count())
        self.assertEqual(0, Absence.objects.all().count())
        self.assertEqual(0, AbsenceReport.objects.all().count())
        self.assertEqual(5, Group.objects.all().count())

    def test_update_activities(self):
        update_resources(self)
        update_activities(self)
        self.assertEqual(4, Student.objects.all().count())
        self.assertEqual(2, Teacher.objects.all().count())
        self.assertEqual(8, Classroom.objects.all().count())
        self.assertEqual(2, Activity.objects.all().count())
        self.assertEqual(28, Event.objects.all().count())
        self.assertEqual(0, Absence.objects.all().count())
        self.assertEqual(0, AbsenceReport.objects.all().count())
        self.assertEqual(5, Group.objects.all().count())

        for student in Student.objects.all():
            print student.name