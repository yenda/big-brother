from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from .views import (SearchView, GroupView, StudentView, TeacherView,
                    ActivityView, HomeView, EventView, ReportView, ValidationView)
from .adeweb import urls as adeweb
from .users import urls as accounts

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts)),
    url(r'^adeweb/', include(adeweb)),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^group/(?P<group>[- \w]+)', GroupView.as_view(), name='group'),
    url(r'^teacher/(?P<teacher>[\w]+)', TeacherView.as_view(), name='teacher'),
    url(r'^student/(?P<student>[\w]+)', StudentView.as_view(), name='student'),
    url(r'^activity/(?P<activity>[- \w]+)', ActivityView.as_view(), name='activity'),
    url(r'^event/(?P<event>[- \w]+)', EventView.as_view(), name='event'),
    url(r'^report/(?P<pk>[- \w]+)', ReportView.as_view(), name='report'),
    url(r'^validation/(?P<code>[- \w]+)', ValidationView.as_view(), name='validation'),
    url(r'^', HomeView.as_view()),
    # Simply show the master template.
    (r'^$', TemplateView.as_view(template_name='master.html')),
)

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)