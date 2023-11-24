from django.db import models
from django.contrib.auth.models import User
import os

from django.urls import reverse
from django.core.exceptions import ValidationError


class Address(models.Model):
    address_name = models.TextField()
    line1 = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.line1}, {self.city}, {self.country}"

class Media(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    MEDIA_TYPES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]

    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES, default=IMAGE)
    file = models.FileField(upload_to='media/%Y/%m/%d/')
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1024, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user = 'sezer-muhammed'
        repo = 'SezerTurizmv2'
        branch = 'main'
        base_path = 'SezerTurizmv2/'  # Base path in the GitHub repository
        image_relative_path = self.file.url  # Relative path from MEDIA_URL
        full_path = os.path.join(base_path, image_relative_path.lstrip('/'))

        raw_url = f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/{full_path}'

        self.image_url = raw_url
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.get_media_type_display()}: {self.file.name}"

class UniversalSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.key}: {self.value}"


class Header(models.Model):
    title = models.CharField(max_length=200)  # For site name or logo text
    logo_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, related_name='header_logos')

    def navbar_links(self):
        # Generate navbar links from sections and subsections
        links = []
        for section in Section.objects.all():
            subsections = Subsection.objects.filter(section=section)
            section_links = {
                'section_name': section.name,
                'subsections': [{'name': ss.name, 'id': ss.id} for ss in subsections]
            }
            links.append(section_links)
        return links

    def __str__(self):
        return self.title


class Footer(models.Model):
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, 
                                limit_choices_to={'address_name': 'Website_Kontakt_Adres'})
    # Other fields or methods as needed

    def get_copyright_text(self):
        try:
            return UniversalSetting.objects.get(key="Website_Footer_Message").value
        except UniversalSetting.DoesNotExist:
            return "Default copyright message"

    def __str__(self):
        return f"Footer - {self.address if self.address else 'No Address'}"

class Section(models.Model):
    name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=100, blank=True, null=True)  # For named URL patterns

    def get_absolute_url(self):
        if self.url_name:
            try:
                return reverse(self.url_name)
            except Exception:
                raise ValidationError(f"Invalid URL name: {self.url_name}")
        else:
            return '#'  # Fallback URL

    def __str__(self):
        return self.name

class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subsections')
    name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        try:
            return reverse(self.url_name)
        except Exception:
            # Fallback URL or handle the error
            return '#'

    def __str__(self):
        return f"{self.section.name} - {self.name}"