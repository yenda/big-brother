__author__ = 'yenda'

from django.views.generic import TemplateView, DetailView

from .models import Lecture


class LectureView(DetailView):
    template_name = 'lectures/lecture.html'
    context_object_name = "lecture"
    model = Lecture

    def get_context_data(self, **kwargs):
        context = super(LectureView, self).get_context_data(**kwargs)
        return context


class UserLecturesView(TemplateView):
    template_name = 'lectures/lectures.html'
    context_object_name = "lectures"

    def get_context_data(self, **kwargs):
        context = super(UserLecturesView, self).get_context_data(**kwargs)
        if self.request.user.is_teacher():
            print "teacher"
            context["lectures"] = Lecture.objects.filter(teachers=self.request.user).distinct()
        else:
            print "not teacher"
            context["lectures"] = Lecture.objects.filter(events__memberships__students=self.request.user).distinct()
        return context