import os

__author__ = 'yenda'
#TODO this file should use a config file instead of hard coded values

from xml.dom.minidom import parse
from urllib.request import urlopen, Request

from .api import GenericApi


class API(GenericApi):
    sessionId = None

    #connects to the adeweb API
    #sets self.sessionId
    def connect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?function=connect&login=ade_projet_etu&password=;projet_2014"
        request = Request(url)
        response = urlopen(request)
        xmldoc = parse(response)
        self.sessionId = xmldoc.getElementsByTagName('session')[0].attributes['id'].value

    def disconnect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=disconnect"
        request = Request(url)
        response = urlopen(request)

        xmldoc = parse(response)
        if xmldoc.getElementsByTagName('disconnected')[0].attributes['sessionId'].value == self.sessionId:
            self.sessionId = None
            return self.sessionId
        return self.sessionId

    def set_project(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=setProject&projectId=13"
        request = Request(url)
        response = urlopen(request)

    def get_resources(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getResources&detail=0"

        request = Request(url)
        resources = urlopen(request).read()

        return resources

    def get_activities(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getActivities&detail=17"

        request = Request(url)
        activities = urlopen(request).read()

        return activities

    def write_resources(self):
        resources = self.get_resources()
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources.xml')
        with open(path, 'wb') as f:
            f.write(resources)

    def write_activities(self):
        activities = self.get_activities()
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../activities.xml')
        with open(path, 'wb') as f:
            f.write(activities)
