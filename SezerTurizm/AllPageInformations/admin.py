from django.contrib import admin
from .models import BrandAwareness, LeadGeneration, LocalAttractions, Informational, CustomerTestimonials

@admin.register(BrandAwareness, LeadGeneration, LocalAttractions, Informational)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)