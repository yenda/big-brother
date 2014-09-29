from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from adeweb import urls as adeweb
from users import urls as accounts
from absences import urls as reports
from cal import urls as calendar
from institution import urls as institution
from lectures import urls as lectures
from home import urls as home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bigbrother.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts)),
    url(r'^adeweb/', include(adeweb)),
    url(r'^reports/', include(reports)),
    url(r'^calendar/', include(calendar)),
    url(r'^institution/', include(institution)),
    url(r'^lectures/', include(lectures)),
    url(r'^/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^', include(home)),
)
