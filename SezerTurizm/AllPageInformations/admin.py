from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (SocialMediaPlatform, FooterMessage, BaseFooter, SocialMediaLink, 
                     Section, Subsection, Subsubsection, NavbarBrand, 
                     Informational, Image, BrandAwareness, LeadGeneration, 
                     LocalAttractions, CustomerTestimonials)
from .translation import *
# Admin classes for each model

@admin.register(SocialMediaPlatform)
class SocialMediaPlatformAdmin(TranslationAdmin):
    list_display = ['name', 'icon_svg']
    search_fields = ['name']

@admin.register(FooterMessage)
class FooterMessageAdmin(TranslationAdmin):
    list_display = ['message', 'footer']
    search_fields = ['message']

@admin.register(BaseFooter)
class BaseFooterAdmin(TranslationAdmin):
    list_display = ['copyright_text', 'locale']
    search_fields = ['copyright_text']

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['footer', 'platform', 'url']
    search_fields = ['platform__name']

@admin.register(Section)
class SectionAdmin(TranslationAdmin):
    list_display = ['name', 'status', 'is_featured', 'order']
    search_fields = ['name']

@admin.register(Subsection)
class SubsectionAdmin(TranslationAdmin):
    list_display = ['name', 'section']
    search_fields = ['name', 'section__name']

@admin.register(Subsubsection)
class SubsubsectionAdmin(TranslationAdmin):
    list_display = ['name', 'subsection']
    search_fields = ['name', 'subsection__name']

@admin.register(NavbarBrand)
class NavbarBrandAdmin(TranslationAdmin):
    list_display = ['name', 'in_use']
    search_fields = ['name']

# For the other models (Informational, Image, etc.)

@admin.register(Informational)
class InformationalAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'get_raw_url']
    search_fields = ['caption']
    fields = ('ref_name', 'image', 'caption', 'created_at')
    readonly_fields = ('ref_name', 'created_at')

    def short_ref_name(self, obj):
        return str(obj.ref_name)
    short_ref_name.short_description = 'Reference Name'

    def get_raw_url(self, obj):
        return obj.image_url
    get_raw_url.short_description = 'Raw URL'




@admin.register(BrandAwareness)
class BrandAwarenessAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']

@admin.register(LeadGeneration)
class LeadGenerationAdmin(TranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']

@admin.register(LocalAttractions)
class LocalAttractionsAdmin(TranslationAdmin):
    list_display = ['title', 'event_date', 'status']
    search_fields = ['title']

@admin.register(CustomerTestimonials)
class CustomerTestimonialsAdmin(TranslationAdmin):
    list_display = ['customer_name', 'rating', 'created_at']
    search_fields = ['customer_name', 'testimonial']
