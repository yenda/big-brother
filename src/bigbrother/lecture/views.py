__author__ = 'yenda'

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Lecture


class TeacherLecturesList(TemplateView):
    template_name = 'classes/teacher-classes.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherLecturesList, self).get_context_data(**kwargs)
        context['activities'] = Lecture.objects.filter(teachers=self.request.user)
        return context


class LectureView(TemplateView):
    template_name = 'classes/activity.html'

    def get_context_data(self, **kwargs):
        context = super(LectureView, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Lecture, id=kwargs["activity"])
        return context