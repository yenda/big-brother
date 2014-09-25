from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, url

from .views import TeacherView, StudentView, ProfileView

urlpatterns = patterns('',
                       url(r'^login/$', auth_views.login, name="login"),
                       url(r'^logout/$',
                           auth_views.logout_then_login, name="logout"),
                       url(r'^password_change/$',
                           auth_views.password_change, {'template_name': 'users/password_change.html'}, name="password_change"),
                       url(r'^password_change_done/$',
                           auth_views.password_change_done, name="password_change_done"),
                       url(r'^$', ProfileView.as_view(), name="profile"),
                       url(r'^teacher/(?P<teacher>[\w]+)', TeacherView.as_view(), name='teacher'),
                       url(r'^student/(?P<student>[\w]+)', StudentView.as_view(), name='student'),
                       )


