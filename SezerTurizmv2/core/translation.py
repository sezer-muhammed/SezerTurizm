from modeltranslation.translator import register, TranslationOptions
from .models import Address, Media, UniversalSetting, Header, Footer, Section, Subsection

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address_name', 'line1', 'city', 'country')

@register(Media)
class MediaTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(UniversalSetting)
class UniversalSettingTranslationOptions(TranslationOptions):
    fields = ('value', 'description')

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Footer)
class FooterTranslationOptions(TranslationOptions):
    fields = ()  # Add fields if you have any translatable content in Footer

@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Subsection)
class SubsectionTranslationOptions(TranslationOptions):
    fields = ('name',)
