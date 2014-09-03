__author__ = 'yenda'
from django.conf.urls import patterns, url

from .views import ReportView, ValidationView

urlpatterns = patterns('',
                       url(r'^report/(?P<pk>[- \w]+)', ReportView.as_view(), name='report'),
                       url(r'^validation/(?P<code>[- \w]+)', ValidationView.as_view(), name='validation'),
                       )


