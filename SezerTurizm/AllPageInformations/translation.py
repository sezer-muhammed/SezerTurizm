from modeltranslation.translator import register, TranslationOptions
from .models import BrandAwareness, LeadGeneration, LocalAttractions, Informational, CustomerTestimonials

@register(BrandAwareness)
class BrandAwarenessTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(LeadGeneration)
class LeadGenerationTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(LocalAttractions)
class LocalAttractionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Informational)
class InformationalTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(CustomerTestimonials)
class CustomerTestimonialsTranslationOptions(TranslationOptions):
    fields = ('testimonial',)
