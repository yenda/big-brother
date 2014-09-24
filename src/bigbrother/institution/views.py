__author__ = 'yenda'

from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property

from ..calendar.models import Event
from . models import Membership


class MembershipView(TemplateView):
    """
        Displays the members of a group
    """
    template_name = 'membership.html'

    @cached_property
    def membership(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(Membership, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(MembershipView, self).get_context_data(**kwargs)
        context['membership'] = self.membership
        context['students'] = get_user_model().objects.filter(memberships=self.membership)

        if context['students']:
            context['number_students'] = len(context['students'])

        context['events'] = Event.objects.filter(memberships=self.membership)[:10]
        return context