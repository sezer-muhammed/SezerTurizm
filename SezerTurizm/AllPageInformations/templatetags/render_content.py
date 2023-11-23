from django import template
from django.template import Context, Template

register = template.Library()

@register.simple_tag(takes_context=True)
def render_template_string(context, template_string):
    return Template(template_string).render(Context(context))
