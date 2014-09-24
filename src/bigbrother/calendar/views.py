__author__ = 'yenda'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from datetime import datetime

from .models import Event


class CalendarView(TemplateView):
    template_name = 'calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        context['today'] = Event.objects.filter(start__gt=datetime.today())
        context['tomorrow'] = Event.objects.filter()
        context['week'] = Event.objects.filter()
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
    template_name = "calendar/create-event.html"
    model = Event