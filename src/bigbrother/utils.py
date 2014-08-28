__author__ = 'yenda'
import urllib2
from xml.dom.minidom import parse
from datetime import datetime

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import Activity
from .models import Student
from .models import Teacher
import xml.sax


class saxParsingResources(xml.sax.ContentHandler):

	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
		self.name = None
		self.student_id = None
		self.groups = []

	def startElement(self, name, attrs):
		if name == "resource":
			if attrs.getValue('category') and attrs.getValue('category') == 'category5':
				self.name = attrs.getValue('name')
				self.student_id = attrs.getValue('id')
				self.groups = []

			elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
				name = attrs.getValue('name')
				teacher_id = attrs.getValue('id')
				teacher = Teacher(name=name, teacher_id=teacher_id)
				teacher.save()

		elif name == "membership":
			self.groups.append(attrs.getValue('name'))
			student = Student(name=self.name, student_id=self.student_id, groups=self.groups)
			student.save()

	def endElement(self, name):
		pass


class saxParsingActivities(xml.sax.ContentHandler):

	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
		self.name = None
		self.student_id = None
		self.groups = []

	def startElement(self, name, attrs):
		if name == "resource":
			if attrs.getValue('category') and attrs.getValue('category') == 'category5':
				self.name = attrs.getValue('name')
				self.student_id = attrs.getValue('id')
				self.groups = []

			elif attrs.getValue('category') and attrs.getValue('category') == 'instructor':
				name = attrs.getValue('name')
				teacher_id = attrs.getValue('id')
				teacher = Teacher(name=name, teacher_id=teacher_id)
				teacher.save()

		elif name == "membership":
			self.groups.append(attrs.getValue('name'))
			student = Student(name=self.name, student_id=self.student_id, groups=self.groups)
			student.save()

	def endElement(self, name):
		pass


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
		xml.sax.parseString(source, saxParsingResources())


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
		dom = parse(response)

		for node in dom.getElementsByTagName('activity'):  # visit every node <activity />

			name = node.getAttribute("name")
			type = node.getAttribute("type")

			for child in node.getElementsByTagName('event'):
				activity_id = child.getAttribute("id")
				date = datetime.strptime(child.getAttribute("date"), "%d/%m/%Y")
				start_time = datetime.strptime(child.getAttribute("startHour"), "%H:%M")
				end_time = datetime.strptime(child.getAttribute("endHour"), "%H:%M")

				groups = []
				teachers = []
				classroom = []
				for participant in child.getElementsByTagName('eventParticipant'):
					if participant.getAttribute("category") == "classroom":
						classroom.append(participant.getAttribute("name"))
					if participant.getAttribute("category") == "instructor":
						teachers.append(participant.getAttribute("id"))
					if participant.getAttribute("category") == "trainee":
						groups.append(participant.getAttribute("name"))

				if groups:
					activity = Activity(name=name,
					                    activity_id=activity_id,
					                    type=type,
					                    date=date,
					                    start_time=start_time,
					                    end_time=end_time,
					                    groups=groups,
					                    teachers=teachers,
					                    classroom=classroom)
					activity.save()


def update_resources(self):
	api = AdewebAPI()
	api.connect()
	api.set_project()
	api.get_resources()
	api.disconnect()
	return redirect(reverse('admin:index'))


def update_activites(self):
	api = AdewebAPI()
	api.connect()
	api.set_project()
	api.get_activities()
	api.disconnect()
	return redirect(reverse('admin:index'))


def delete_data(self):
	Teacher.objects.all().delete()
	Activity.objects.all().delete()
	Student.objects.all().delete()
	return redirect(reverse('admin:index'))
