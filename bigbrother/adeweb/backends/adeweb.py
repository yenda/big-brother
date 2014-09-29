__author__ = 'yenda'
#TODO this file should use a config file instead of hard coded values

from xml.dom.minidom import parse
from urllib.request import urlopen, Request


class API(object):
    sessionId = None

    #connects to the adeweb API
    #sets self.sessionId
    def connect(self):
        url = b"https://adeweb.univ-lorraine.fr/jsp/webapi?function=connect&login=ade_projet_etu&password=;projet_2014"
        response = urlopen(url)

        xmldoc = parse(response)
        self.sessionId = xmldoc.getElementsByTagName('session')[0].attributes['id'].value

    def disconnect(self):
        url = b"https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=disconnect"
        response = urlopen(url)

        xmldoc = parse(response)
        if xmldoc.getElementsByTagName('disconnected')[0].attributes['sessionId'].value == self.sessionId:
            self.sessionId = None
            return self.sessionId
        return self.sessionId

    def set_project(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=setProject&projectId=9"
        response = urlopen(url)

    def get_resources(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getResources&detail=0"

        request = Request(url)

        return request

    def get_activities(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getActivities&detail=17"

        request = Request(url)

        return request