from django.db import models
from AllPageInformations.models import Subsubsection

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField()  # For a brief description or summary
    html_content = models.TextField()
    symbolic_image_url = models.URLField(blank=True)
    subsubsection = models.ForeignKey(
        Subsubsection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events'
    )

    def __str__(self):
        return self.title