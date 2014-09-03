__author__ = 'yenda'

from django.views.generic import DetailView, View
from django.shortcuts import get_object_or_404, redirect

from .models import AbsenceReport, Absence


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