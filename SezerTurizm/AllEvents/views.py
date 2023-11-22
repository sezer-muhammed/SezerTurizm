from django.views.generic import TemplateView
from django.utils import timezone
from .models import Event
from AllPageInformations.models import Image

class EventsHomeView(TemplateView):
    template_name = 'events/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()

        return context