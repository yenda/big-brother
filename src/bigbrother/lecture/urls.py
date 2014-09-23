from django.conf.urls import patterns, url

from .views import LectureView

urlpatterns = patterns('',
                       url(r'^(?P<lecture>[- \w]+)', LectureView.as_view(), name='lecture'),
                       )
