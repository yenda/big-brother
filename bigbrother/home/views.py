__author__ = 'yenda'

from datetime import datetime

from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

from .forms import SearchForm
from institution.models import Membership
from cal.models import Event


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get('name')
        context['form'] = SearchForm
        if search:
            context['search'] = search
            context['teachers'] = get_user_model().objects.filter(username__icontains=search, lecture__isnull=False).distinct().orderby('last_name')
            context['students'] = get_user_model().objects.filter(username__icontains=search, lecture__isnull=True).distinct().orderby('last_name')
            context['memberships'] = Membership.objects.filter(name__icontains=search)

            results = len(context['teachers']) + len(context['students']) + len(context['memberships'])
            if results > 0:
                context['results'] = results
        else:
            context['events'] = Event.objects.filter(start__lte=datetime.today(),
                                                     end__gte=datetime.today())
        return context