from django.views.generic import TemplateView
from django.utils import timezone
from .models import Event

class EventsHomeView(TemplateView):
    template_name = 'events/home.html'  # Your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch your events here, you can customize the query as needed
        context['events'] = Event.objects.all()  # Or any other query
        return context
