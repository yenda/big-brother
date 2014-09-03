from django.conf.urls import patterns, url

from .views import MembershipView
urlpatterns = patterns('',
                       url(r'^membership/(?P<membership>[- \w]+)', MembershipView.as_view(), name='membership'),
                       )