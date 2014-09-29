from django.conf.urls import patterns, url

from .views import EventView, CreateEventView, CalendarView

urlpatterns = patterns('',
                       url(r'^$', CalendarView.as_view(), name='calendar'),
                       url(r'^event/create/$', CreateEventView.as_view(), name='create-event'),
                       url(r'^event/(?P<event>[- \w]+)/', EventView.as_view(), name='event'),
                       )
