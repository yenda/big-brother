__author__ = 'yenda'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Activity, Event


class ActivityView(TemplateView):
    template_name = 'activity.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityView, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, id=kwargs["activity"])
        return context


class EventView(TemplateView):
    template_name = 'calendar/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, adeweb_id=kwargs["event"])
        context['teachers'] = get_user_model().objects.filter(events=context["event"])
        context['students'] = get_user_model().objects.filter(memberships__events=context["event"])
        return context


class CreateEventView(CreateView):
    template_name = "create-event.html"
    model = Event