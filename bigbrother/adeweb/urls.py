__author__ = 'yenda'

from django.conf.urls import patterns, url
from .views import (update_activities, update_resources, delete_data)

urlpatterns = patterns('',
    url(r'^updateresources/$', update_resources, name='updateResources'),
    url(r'^updateactivities/$', update_activities, name='updateActivities'),
    url(r'^deletedata/$', delete_data, name='deleteData'),
)