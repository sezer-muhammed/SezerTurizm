import os
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
import reversion
import random
from django.core.cache import cache
import uuid

class Colors(models.Model):
    primary = models.CharField(max_length=7, default='#0d6efd')  # Default Bootstrap Primary
    secondary = models.CharField(max_length=7, default='#6c757d')  # Default Bootstrap Secondary
    success = models.CharField(max_length=7, default='#198754')  # Default Bootstrap Success
    danger = models.CharField(max_length=7, default='#dc3545')  # Default Bootstrap Danger
    warning = models.CharField(max_length=7, default='#ffc107')  # Default Bootstrap Warning
    info = models.CharField(max_length=7, default='#0dcaf0')  # Default Bootstrap Info
    light = models.CharField(max_length=7, default='#f8f9fa')  # Default Bootstrap Light
    dark = models.CharField(max_length=7, default='#212529')  # Default Bootstrap Dark
    text = models.CharField(max_length=7, default='#212529')  # Default text color
    header = models.CharField(max_length=7, default='#f8f9fa')  # Default header color
    complementary = models.CharField(max_length=7, default='#ffffff')  # Additional complementary color
    body_bg = models.CharField(max_length=7, default='#ffffff')  # Body background color
    body_color = models.CharField(max_length=7, default='#212529')  # Body text color


#* For footer

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=50)
    icon_svg = models.TextField(help_text="SVG content for the icon")
    url_template = models.CharField(max_length=255, help_text="URL template for user-specific pages (e.g., 'https://twitter.com/{}')")

    def __str__(self):
        return self.name

class FooterMessage(models.Model):
    message = RichTextField()
    footer = models.ForeignKey('BaseFooter', related_name='messages', on_delete=models.CASCADE)
    display_condition = models.JSONField(default=dict, help_text="Conditions for displaying the message")

    def __str__(self):
        return self.message

class BaseFooter(models.Model):
    social_media = models.ManyToManyField(SocialMediaPlatform, through='SocialMediaLink')
    copyright_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    locale = models.CharField(max_length=10, default='tr', help_text="Locale for multi-language support")

    @classmethod
    def get_random_message(cls):
        """Get a random footer message."""
        random_message = cache.get('random_footer_message')

        if not random_message:
            try:
                instance = cls.objects.prefetch_related('messages').first()
                messages = [msg.message for msg in instance.messages.all()]
                random_message = random.choice(messages)
                cache.set('random_footer_message', random_message, 300)  # cache for 5 minutes
            except (cls.DoesNotExist, IndexError):
                random_message = ""

        return random_message

class SocialMediaLink(models.Model):
    footer = models.ForeignKey(BaseFooter, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform.name} link for footer"

class Section(models.Model):
    name = models.CharField(max_length=255)
    link = models.TextField()
    image = models.ImageField(upload_to='sections/')
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    description = models.TextField()
    html_content = models.TextField()
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Order in which the section appears")
    visibility_rules = models.JSONField(default=dict, help_text="Rules for when the section is visible")
    seo_metadata = models.JSONField(default=dict, help_text="SEO metadata for the section")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Subsection(models.Model):
    name = models.CharField(max_length=255)
    link = models.TextField()
    section = models.ForeignKey(Section, related_name='subsections', on_delete=models.CASCADE)
    breadcrumb = models.TextField(help_text="Automatically generated breadcrumb navigation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Subsubsection(models.Model):
    name = models.CharField(max_length=255)
    link = models.TextField()
    subsection = models.ForeignKey(Subsection, related_name='subsubsections', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class NavbarBrand(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    logo = models.ImageField(upload_to='brand_logos/', null=True, blank=True)
    in_use = models.BooleanField(default=False)
    version_history = models.JSONField(default=list, help_text="Version history of the brand")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@reversion.register
class Informational(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ref_name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    image_url = models.URLField(max_length=1024, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user = 'sezer-muhammed'
        repo = 'SezerTurizm'
        branch = 'main'
        base_path = 'SezerTurizm/'  # Base path in the GitHub repository
        image_relative_path = self.image.url  # Relative path from MEDIA_URL
        full_path = os.path.join(base_path, image_relative_path.lstrip('/'))

        raw_url = f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/{full_path}'

        self.image_url = raw_url
        super().save(*args, **kwargs)

class BrandAwareness(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField("Image", related_name='brand_awareness')
    slug = models.SlugField(unique=True)
    meta_description = models.CharField(max_length=160, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class LeadGeneration(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class LocalAttractions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField("Image", related_name='local_attractions')
    tags = TaggableManager()
    event_date = models.DateField()
    status = models.CharField(max_length=100, choices=[('upcoming', 'Upcoming'), ('past', 'Past')])
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerTestimonials(models.Model):
    customer_name = models.CharField(max_length=100)
    testimonial = models.TextField()
    images = models.ManyToManyField("Image", related_name='testimonials')
    rating = models.PositiveSmallIntegerField(default=5)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)