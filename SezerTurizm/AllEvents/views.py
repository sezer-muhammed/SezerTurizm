from django.views.generic import TemplateView
from django.utils import timezone
from .models import Event
from AllPageInformations.models import Image

class EventsHomeView(TemplateView):
    template_name = 'events/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()

        events_images = Image.objects.all()
        if events_images.exists():
            context['first_event_image_url'] = events_images.first().image.url
            print(events_images.first().image_url)
        else:
            context['first_event_image_url'] = None  # or a default image URL
            print(context['first_event_image_url'])
        return context