from django.views.generic import TemplateView
from django.utils import timezone
from .models import Event
from AllPageInformations.models import Image
from .variables import FILTER_KEYWORDS
from django.http import Http404


class EventsHomeView(TemplateView):
    template_name = 'events/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_keyword = self.kwargs.get('filter_keyword')
        if filter_keyword:
            subsection_id = FILTER_KEYWORDS.get(filter_keyword)

            if subsection_id:
                filtered_events = Event.objects.filter(subsubsection__subsection_id=subsection_id)
                context['events'] = filtered_events
            else:
                # Raise 404 only if a keyword is provided but it doesn't match
                raise Http404("Page not found.")
        else:
            # If no filter keyword is supplied, return all events
            context['events'] = Event.objects.all()

        return context