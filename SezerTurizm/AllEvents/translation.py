from modeltranslation.translator import register, TranslationOptions
from .models import Event

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'description', 'html_content',)
