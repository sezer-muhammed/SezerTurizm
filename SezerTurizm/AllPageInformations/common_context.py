from .models import BaseFooter, FooterMessage, SocialMediaLink, Section, NavbarBrand, Colors

def common_context(request):
    """Provide common context data to all templates."""
    base_footer = BaseFooter.objects.first()
    random_message = FooterMessage.objects.order_by('?').first()
    social_media_links = SocialMediaLink.objects.all()
    sections = Section.objects.prefetch_related('subsections__subsubsections').all()
    navbar_brand = NavbarBrand.objects.filter(in_use=True).last()

    return {
        'base_footer': base_footer,
        'random_message': random_message.message if random_message else None,
        'social_media_links': social_media_links,
        'sections': sections,
        'navbar_brand': navbar_brand,
    }
