from django.urls import path
from .views import EventsHomeView

urlpatterns = [
    # ... other URL patterns ...
    path('', EventsHomeView.as_view(), name='events-home'),
]
