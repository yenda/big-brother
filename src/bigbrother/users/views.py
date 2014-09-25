from django.conf.global_settings import AUTH_USER_MODEL
from django.core.urlresolvers import reverse, reverse_lazy

__author__ = 'yenda'

from django.views.generic import TemplateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from ..calendar.models import Event


class StudentView(TemplateView):
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(AUTH_USER_MODEL, pk=kwargs["student"])
        context['events'] = Event.objects.filter(memberships__students=context['student'])
        return context


class TeacherView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['teacher'] = get_object_or_404(AUTH_USER_MODEL, adeweb_id=kwargs["teacher"])
        context['events'] = Event.objects.filter(teachers=context["teacher"])
        return context


class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.request.user.pk)