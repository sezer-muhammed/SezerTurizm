from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event
from .translation import *
from django.utils.safestring import mark_safe

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['title', 'date', 'location']
    search_fields = ['title', 'description']
    readonly_fields = ['html_content_preview']

    def html_content_preview(self, obj):
        return mark_safe(obj.html_content)
    html_content_preview.short_description = 'HTML Content Preview'
    html_content_preview.allow_tags = True
