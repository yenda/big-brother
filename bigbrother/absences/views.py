__author__ = 'yenda'

from django.views.generic import FormView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from datetime import datetime

from lectures.models import Lecture
from cal.models import Event
from institution.models import Membership
from .forms import ReportForm
from .models import Absence


class EventMixin(object):
    @cached_property
    def event(self):
        pk = self.kwargs.get("event")
        if not pk:
            absence = get_object_or_404(Absence, pk=self.kwargs.get("pk"))
            pk = absence.event.pk
        return get_object_or_404(Event, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(EventMixin, self).get_context_data(**kwargs)
        context["event"] = self.event
        return context


class RestrictedEventMixin(EventMixin):
    """
        Restricted view : teachers in self.event.lecture and admins only
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser and not self.request.user.is_teacher_in(self.event.lecture):
            return redirect('event-report', self.event.pk)
        return super(RestrictedEventMixin, self).dispatch(*args, **kwargs)


class EventReportView(EventMixin, TemplateView):
    template_name = 'absences/event-absences.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(EventReportView, self).get_context_data()
        context['absences'] = Absence.objects.filter(event=self.event)
        return context


class EventCreateReportView(RestrictedEventMixin, FormView):
    """
        Restricted view : teachers in self.event.lecture and admins only
    """
    template_name = 'absences/event-create-absences.html'
    form_class = ReportForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(EventCreateReportView, self).get_form_kwargs()
        kwargs["event"] = self.event
        return kwargs

    def form_valid(self, form):
        self.event.report = True
        self.event.save()
        for student in form.cleaned_data["students"]:
            Absence.objects.get_or_create(student=student, event=self.event)
        return super(EventCreateReportView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['event']
        return reverse('event-report', args=(pk,))


class AbsenceUpdateView(RestrictedEventMixin, UpdateView):
    template_name = "absences/absence-update.html"
    fields = ["excuse", ]
    model = Absence

    def get_success_url(self):
        pk = self.kwargs['pk']
        absence = get_object_or_404(Absence, pk=pk)
        return reverse('event-report', args=(absence.event.pk,))


class AbsenceDeleteView(RestrictedEventMixin, DeleteView):
    template_name = "absences/absence-delete.html"
    model = Absence

    def get_success_url(self):
        pk = self.kwargs['pk']
        absence = get_object_or_404(Absence, pk=pk)
        return reverse('event-report', args=(absence.event.pk,))


class StudentAbsenceList(TemplateView):
    model = Absence

    def get_queryset(self):
        pass


class AbsenceLectureView(TemplateView):
    template_name = "absences/absence-lecture.html"
    model = Absence

    @cached_property
    def lecture(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Lecture, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(AbsenceLectureView, self).get_context_data()
        context["lecture"] = self.lecture
        context["events"] = Event.objects.filter(lecture=self.lecture, start__lte=datetime.today()).order_by("start")
        context["absences"] = Absence.objects.filter(event__lecture=self.lecture)
        return context


class AbsenceMembershipView(TemplateView):
    template_name = "absences/absence-membership.html"

    @cached_property
    def membership(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Membership, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(AbsenceMembershipView, self).get_context_data()
        context["membership"] = self.membership
        context["events"] = Event.objects.filter(memberships=self.membership).order_by("start")
        context["absences"] = Absence.objects.filter(event__memberships=self.membership)
        return context


class AbsenceStudentView(TemplateView):
    template_name = "absences/absence-student.html"

    @cached_property
    def student(self):
        pk = self.kwargs['pk']
        return get_object_or_404(get_user_model(), pk=pk)

    def get_context_data(self, **kwargs):
        context = super(AbsenceStudentView, self).get_context_data()
        context["student"] = self.student
        context["absences"] = Absence.objects.filter(student=self.student).order_by("-event__start")
        context["excused"] = Absence.objects.filter(student=self.student).exclude(excuse="").count()
        return context