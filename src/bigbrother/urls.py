from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from .views import (SearchView, GroupView, StudentView, TeacherView, ActivityView, HomeView)
from .utils import (update_activites, update_resources, delete_data)

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^updateresources', update_resources, name='updateResources'),
    url(r'^updateactivities', update_activites, name='updateActivities'),
    url(r'^deletedata', delete_data, name='deleteData'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^group/(?P<group>[- \w]+)', GroupView.as_view(), name='group'),
    url(r'^teacher/(?P<teacher>[\w]+)', TeacherView.as_view(), name='teacher'),
    url(r'^student/(?P<student>[\w]+)', StudentView.as_view(), name='student'),
    url(r'^activity/(?P<activity>[- \w]+)', ActivityView.as_view(), name='activity'),
    url(r'^', HomeView.as_view()),
    # Simply show the master template.
    (r'^$', TemplateView.as_view(template_name='master.html')),
)

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)