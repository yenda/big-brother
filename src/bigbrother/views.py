__author__ = 'yenda'
from django.views.generic import TemplateView
from django.db.models import Q
from datetime import datetime
from django.shortcuts import get_object_or_404
from .forms import SearchForm
from .models import Student
from .models import Activity
from .models import Teacher
from .models import Group


class HomeView(TemplateView):
    template_name = 'home.html'


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get('name')
        context['form'] = SearchForm
        if search:
            context['search'] = search
            context['teachers'] = Teacher.objects.filter(name__icontains=search)
            context['students'] = Student.objects.filter(name__icontains=search)
            context['group'] = Group.objects.filter(name__icontains=search)

            results = len(context['teachers']) + len(context['students']) + len(context['group'])
            if results > 0:
                context['results'] = results
        return context


class GroupView(TemplateView):
    template_name = 'group.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['students'] = Student.object.filter(groups_name__icontains=kwargs["group"])

        if context['students']:
            context['number_students'] = len(context['students'])

        context['group'] = kwargs["group"]
        context['activities'] = Activity.objects.filter(groups__icontains=kwargs["group"], date=datetime.now().date()).order_by('end_time')[:10]
        return context


class StudentView(TemplateView):
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(Student, student_id=kwargs["student"])
        groups = str.split(context['student'].groups, ",")
        filters = []
        for group in groups:
            filters.append(Q(groups__icontains=group))
        q = Q()
        for f in filters:
            q |= f
        context['activities'] = Activity.objects.filter(q)
        return context


class TeacherView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['teacher'] = get_object_or_404(Teacher, teacher_id=kwargs["teacher"])
        context['activities'] = Activity.objects.filter(teachers__icontains=kwargs["teacher"])
        return context


class ActivityView(TemplateView):
    template_name = 'activity.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityView, self).get_context_data(**kwargs)
        context['activity'] = get_object_or_404(Activity, activity_id=kwargs["activity"])
        return context