from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, url

from .views import TeacherView, StudentView

urlpatterns = patterns('',
                       url(r'^login/$', auth_views.login, name="login"),
                       url(r'^logout/$',
                           auth_views.logout_then_login, name="logout"),
                       url(r'^teacher/(?P<teacher>[\w]+)', TeacherView.as_view(), name='teacher'),
                       url(r'^student/(?P<student>[\w]+)', StudentView.as_view(), name='student'),
                       )


