__author__ = 'yenda'

from django.views.generic import TemplateView, View, DetailView
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from .forms import SearchForm
from .models import Activity, Event, AbsenceReport, Absence, Membership
from django.contrib.auth import get_user_model


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
            context['teachers'] = get_user_model().objects.filter(username__icontains=search, category="instructor")
            context['students'] = get_user_model().objects.filter(username__icontains=search, category="student")
            context['groups'] = Membership.objects.filter(name__icontains=search)

            results = len(context['teachers']) + len(context['students']) + len(context['groups'])
            if results > 0:
                context['results'] = results
        else:
            context['events'] = Event.objects.filter(start__lte=datetime.today(),
                                                     end__gte=datetime.today())
        return context


class GroupView(TemplateView):
    template_name = 'group.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['students'] = get_user_model().objects.filter(groups__name__icontains=kwargs["group"])

        if context['students']:
            context['number_students'] = len(context['students'])

        context['group'] = kwargs["group"]
        context['activities'] = Event.objects.filter(groups__name__icontains=kwargs["group"])[:10]
        return context


class StudentView(TemplateView):
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['student'] = get_object_or_404(get_user_model(), adeweb_id=kwargs["student"])
        context['events'] = Event.objects.filter(groups__students=context['student'])
        return context


class TeacherView(TemplateView):
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['teacher'] = get_object_or_404(get_user_model(), adeweb_id=kwargs["teacher"])
        context['events'] = Event.objects.filter(teachers=context["teacher"])
        return context


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
        context['students'] = get_user_model().objects.filter(groups__events=context["event"])
        return context


class ReportView(DetailView):
    template_name = 'report.html'
    model = AbsenceReport
    context_object_name = "report"


class ValidationView(View):
    def get(self, request, *args, **kwargs):
        report = get_object_or_404(AbsenceReport, code=kwargs["code"])
        for student in report.students.all():
            Absence(student=student, event=report.event).save()
            report.validated = True
            report.save()
        return redirect(report)