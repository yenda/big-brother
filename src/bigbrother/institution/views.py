__author__ = 'yenda'

from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from ..calendar.models import Event


class MembershipView(TemplateView):
    template_name = 'membership.html'

    def get_context_data(self, **kwargs):
        context = super(MembershipView, self).get_context_data(**kwargs)
        context['students'] = get_user_model().objects.filter(memberships__name__icontains=kwargs["group"])

        if context['students']:
            context['number_students'] = len(context['students'])

        context['membership'] = kwargs["membership"]
        context['activities'] = Event.objects.filter(memberships__name__icontains=kwargs["membership"])[:10]
        return context