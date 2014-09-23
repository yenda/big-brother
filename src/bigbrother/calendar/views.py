__author__ = 'yenda'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Event
from ..lecture.models import Lecture


class TeacherActivityList(TemplateView):
    template_name = 'calendar/teacher-classes.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherActivityList, self).get_context_data(**kwargs)
        context['activities'] = Lecture.objects.filter(teachers=self.request.user)
        return context


class ActivityView(TemplateView):
    template_name = 'calendar/activity.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityView, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Lecture, id=kwargs["activity"])
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