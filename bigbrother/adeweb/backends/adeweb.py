__author__ = 'yenda'
#TODO this file should use a config file instead of hard coded values

from xml.dom.minidom import parse
from urllib3.request import urlopen



class API(object):
    sessionId = None

    #connects to the adeweb API
    #sets self.sessionId
    def connect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?function=connect&login=ade_projet_etu&password=;projet_2014"
        response = urlopen(url)
        xmldoc = parse(response)
        self.sessionId = xmldoc.getElementsByTagName('session')[0].attributes['id'].value

    def disconnect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=disconnect"
        response = urlopen(url)

        xmldoc = parse(response)
        if xmldoc.getElementsByTagName('disconnected')[0].attributes['sessionId'].value == self.sessionId:
            self.sessionId = None
            return self.sessionId
        return self.sessionId

    def set_project(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=setProject&projectId=9"
        response = urlopen(url)

        project = response.read()
        return project

    def get_resources(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getResources&detail=0"
        response = urlopen(url)

        source = response.read()
        return source

    def get_activities(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getActivities&detail=17"
        response = urlopen(url)

        source = response.read()
        return source