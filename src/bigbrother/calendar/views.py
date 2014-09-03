__author__ = 'yenda'

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Activity, Event
from ..absences.models import AbsenceReport


class ActivityView(TemplateView):
    template_name = 'activity.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityView, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, id=kwargs["activity"])
        return context


import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class EventView(TemplateView):
    template_name = 'event.html'

    def post(self, request, *args, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, adeweb_id=kwargs["event"])
        context['teachers'] = get_user_model().objects.filter(events=context["event"])
        students_id = self.request.POST.getlist("students")
        context['students'] = get_user_model().objects.filter(groups__events=context["event"], adeweb_id__in=students_id)
        if students_id:
            code = id_generator(30)
            absence_report = AbsenceReport(code=code, event=context['event'])
            absence_report.save()
            for student in context["students"]:
                absence_report.students.add(student)
            context["success"] = True
            context["link"] = "/validation/"+code
        context["message"] = True
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, adeweb_id=kwargs["event"])
        context['teachers'] = get_user_model().objects.filter(events=context["event"])
        context['students'] = get_user_model().objects.filter(memberships__events=context["event"])
        return context