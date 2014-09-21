

__author__ = 'yenda'

from django.views.generic import FormView

from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property

from ..calendar.models import Event
from .forms import ReportForm
from .models import Absence


class EventCreateReportView(FormView):
    template_name = 'reports/event-report.html'
    form_class = ReportForm
    success_url = "/"

    @cached_property
    def event(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Event, pk=pk)

    def get_form_kwargs(self):
        kwargs = super(EventCreateReportView, self).get_form_kwargs()
        kwargs["event"] = self.event
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(EventCreateReportView, self).get_context_data()
        context["event"] = self.event
        context["form"] = self.form_class(event=self.event)
        return context

    def form_valid(self, form):
        self.event.report = True
        self.event.save()
        for student in form.cleaned_data["students"]:
            Absence(student=student, event=self.event).save()
        return super(EventCreateReportView, self).form_valid(form)
