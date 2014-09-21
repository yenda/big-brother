__author__ = 'yenda'
from django.conf.urls import patterns, url

from .views import EventCreateReportView

urlpatterns = patterns('',
                       url(r'^event/(?P<pk>[- \w]+)$', EventCreateReportView.as_view(), name='event-report'),
                       )


