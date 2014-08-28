__author__ = 'yenda'
#TODO this file should use a config file instead of hard coded values

from xml.dom.minidom import parse
import urllib2


class AdewebAPI(object):
    sessionId = None

    #connects to the adeweb API
    #sets self.sessionId
    def connect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?function=connect&login=ade_projet_etu&password=;projet_2014"
        request = urllib2.Request(url)
        #gerer exception
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return None
        except urllib2.URLError:
            return None
        xmldoc = parse(response)
        self.sessionId = xmldoc.getElementsByTagName('session')[0].attributes['id'].value

    def disconnect(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=disconnect"
        request = urllib2.Request(url)
        #gerer exception
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return self.sessionId
        except urllib2.URLError:
            return self.sessionId
        xmldoc = parse(response)
        if xmldoc.getElementsByTagName('disconnected')[0].attributes['sessionId'].value == self.sessionId:
            self.sessionId = None
            return self.sessionId
        return self.sessionId

    def set_project(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=setProject&projectId=9"
        request = urllib2.Request(url)
        #gerer exception
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return None
        except urllib2.URLError:
            return None
        project = response.read()
        return project

    def get_resources(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getResources&detail=0"
        request = urllib2.Request(url)
        #gerer exception
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return None
        except urllib2.URLError:
            return None
        source = response.read()
        with open("resources.xml") as f:
            f.write(source)
        return source

    def get_activities(self):
        url = "https://adeweb.univ-lorraine.fr/jsp/webapi?sessionId="+self.sessionId+"&function=getActivities&detail=17"
        request = urllib2.Request(url)
        #gerer exception
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            return None
        except urllib2.URLError:
            return None
        source = response.read()
        return source