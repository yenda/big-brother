from django.conf.urls import patterns, url

from .views import LectureView, UserLecturesView

urlpatterns = patterns('',
                       url(r'^$', UserLecturesView.as_view(), name='lectures'),
                       url(r'^(?P<pk>[- \w]+)$', LectureView.as_view(), name='lecture'),
                       )
