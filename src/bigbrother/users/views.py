__author__ = 'yenda'

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from ..calendar.models import Event


class StudentView(TemplateView):
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(get_user_model(), pk=kwargs["student"])
        context['events'] = Event.objects.filter(memberships__students=context['student'])
        return context


class TeacherView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['teacher'] = get_object_or_404(get_user_model(), adeweb_id=kwargs["teacher"])
        context['events'] = Event.objects.filter(teachers=context["teacher"])
        return context