__author__ = 'yenda'

from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from .views import SearchView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^search$', SearchView.as_view(), name='search'),
    # Simply show the master template.
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^privacy$', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    url(r'^terms$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    )