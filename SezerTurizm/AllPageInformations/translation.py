from modeltranslation.translator import register, TranslationOptions
from .models import (SocialMediaPlatform, FooterMessage, BaseFooter, 
                     Section, Subsection, Subsubsection, NavbarBrand, 
                     Informational, BrandAwareness, LeadGeneration, 
                     LocalAttractions, CustomerTestimonials, HomePageSectionTitles)

@register(HomePageSectionTitles)
class HomePageSectionTitlesTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle') 

@register(SocialMediaPlatform)
class SocialMediaPlatformTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(FooterMessage)
class FooterMessageTranslationOptions(TranslationOptions):
    fields = ('message',)

@register(BaseFooter)
class BaseFooterTranslationOptions(TranslationOptions):
    fields = ('copyright_text',)

# Note: SocialMediaLink may not need translation as it primarily contains URLs.

@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'html_content', 'seo_metadata')

@register(Subsection)
class SubsectionTranslationOptions(TranslationOptions):
    fields = ('name', 'breadcrumb')

@register(Subsubsection)
class SubsubsectionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(NavbarBrand)
class NavbarBrandTranslationOptions(TranslationOptions):
    fields = ('name', 'version_history')

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
