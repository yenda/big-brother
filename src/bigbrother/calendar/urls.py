from django.conf.urls import patterns, url

from .views import ActivityView, EventView, CreateEventView

urlpatterns = patterns('',
                       url(r'^activity/(?P<activity>[- \w]+)', ActivityView.as_view(), name='activity'),
                       url(r'^event/create/$', CreateEventView.as_view(), name='create-event'),
                       url(r'^event/(?P<event>[- \w]+)', EventView.as_view(), name='event'),
                       )
