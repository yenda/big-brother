__author__ = 'yenda'

from django.conf.urls import patterns, url

from .views import (EventCreateReportView, EventReportView, AbsenceUpdateView, AbsenceDeleteView,
                    AbsenceLectureView, AbsenceMembershipView, AbsenceStudentView)

urlpatterns = patterns('',
                       url(r'^absences/event/(?P<event>[- \w]+)$', EventReportView.as_view(), name='event-report'),
                       url(r'^absences/event/(?P<event>[- \w]+)/create$', EventCreateReportView.as_view(), name='event-create-report'),
                       url(r'^absences/(?P<pk>[- \w]+)/update$', AbsenceUpdateView.as_view(), name='absence-update'),
                       url(r'^absences/(?P<pk>[- \w]+)/delete$', AbsenceDeleteView.as_view(), name='absence-delete'),
                       url(r'^absences/lecture/(?P<pk>[- \w]+)$', AbsenceLectureView.as_view(), name='absence-lecture'),
                       url(r'^absences/student/(?P<pk>[- \w]+)$', AbsenceStudentView.as_view(), name='absence-student'),
                       url(r'^absences/membership/(?P<pk>[- \w]+)$', AbsenceMembershipView.as_view(), name='absence-membership'),
                       )


