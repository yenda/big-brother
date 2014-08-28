__author__ = 'yenda'

from django.test.utils import override_settings
from django.test import TestCase
from django.test import Client

from ...models import (Student, Teacher, Classroom, Activity, Absence, AbsenceReport, Group)
from ..views import update_resources

@override_settings(ADEWEB_API={
    'BACKEND': 'bigbrother.adeweb.backends.dummy.API',
})
class ParsingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_resources(self):
        url = "/adeweb/updateResources"
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200, "User could not access the page %s" % url)
        update_resources(self)
        print "number of Student : %s" % Student.objects.all().count()
        print "number of Teacher : %s" % Teacher.objects.all().count()
        print "number of Classroom : %s" % Classroom.objects.all().count()
        print "number of Activity : %s" % Activity.objects.all().count()
        print "number of Absence : %s" % Absence.objects.all().count()
        print "number of AbsenceReport : %s" % AbsenceReport.objects.all().count()
        print "number of Group : %s" % Group.objects.all().count()