__author__ = 'yenda'

from django.conf.urls import patterns, url

from .views import EventCreateReportView, EventReportView, AbsenceUpdateView, AbsenceDeleteView

urlpatterns = patterns('',
                       url(r'^event/(?P<event>[- \w]+)$', EventReportView.as_view(), name='event-report'),
                       url(r'^event/(?P<event>[- \w]+)/create$', EventCreateReportView.as_view(), name='event-create-report'),
                       url(r'^absence/(?P<pk>[- \w]+)/update', AbsenceUpdateView.as_view(), name='absence-update'),
                       url(r'^absence/(?P<pk>[- \w]+)/delete', AbsenceDeleteView.as_view(), name='absence-delete'),
                       )


