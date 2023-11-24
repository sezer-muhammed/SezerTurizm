from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Address, Media, UniversalSetting, Header, Footer, Section, Subsection

from .translation import *

@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ('address_name', 'line1', 'city', 'country')

@admin.register(Media)
class MediaAdmin(TranslationAdmin):
    list_display = ('media_type', 'description', 'image_url')
    list_filter = ('media_type',)

@admin.register(UniversalSetting)
class UniversalSettingAdmin(TranslationAdmin):
    list_display = ('key', 'value', 'description')

@admin.register(Header)
class HeaderAdmin(TranslationAdmin):
    list_display = ('title',)
    # Note: Since 'logo_image' is a ForeignKey, it doesn't need translation handling here

@admin.register(Footer)
class FooterAdmin(TranslationAdmin):
    list_display = ('address',)
    # Additional fields or methods as needed

@admin.register(Section)
class SectionAdmin(TranslationAdmin):
    list_display = ('name', 'url_name')
    search_fields = ('name',)

@admin.register(Subsection)
class SubsectionAdmin(TranslationAdmin):
    list_display = ('name', 'section')
    list_filter = ('section',)
    search_fields = ('name', 'section__name')
