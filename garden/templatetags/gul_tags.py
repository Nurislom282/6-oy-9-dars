from django import template

from ..models import Turlar

register = template.Library()


@register.simple_tag
def get_turs():
    return Turlar.objects.all()