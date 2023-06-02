from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def mediapath(image_path):
    return f"{settings.MEDIA_URL}{image_path}"


@register.filter(needs_autoescape=True)
def short_description(text, autoescape=True):
    result = text[:100]
    return mark_safe(result)