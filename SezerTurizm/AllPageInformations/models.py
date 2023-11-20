from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
import reversion

@reversion.register
class Informational(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

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