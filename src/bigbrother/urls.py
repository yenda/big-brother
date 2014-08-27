from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Simply show the master template.
    (r'^$', TemplateView.as_view(template_name='master.html')),
)

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
