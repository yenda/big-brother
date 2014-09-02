from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, url
from django.http import request

urlpatterns = patterns('',
                       url(r'^login/$', auth_views.login, name="login"),
                       url(r'^logout/$',
                           auth_views.logout_then_login, name="logout"),
                       )

