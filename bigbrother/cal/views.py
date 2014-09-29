__author__ = 'yenda'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Event


class CalendarView(TemplateView):
    template_name = 'calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        #context['today'] = Event.objects.filter(start__gt=date.today(), start__lte=date.today() + timedelta(days=1))
        context['events'] = Event.objects.filter(teacher=self.request.user, memberships_students=self.request.user)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CalendarView, self).dispatch(request, *args, **kwargs)


class EventView(TemplateView):
    template_name = 'calendar/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=kwargs["event"])
        context['teachers'] = get_user_model().objects.filter(events=context["event"])
        context['students'] = get_user_model().objects.filter(memberships__events=context["event"])
        return context


class CreateEventView(CreateView):
    template_name = "calendar/create-event.html"
    model = Event