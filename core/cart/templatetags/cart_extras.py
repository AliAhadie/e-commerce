
from django import template

register = template.Library()

@register.filter
def number_range(value):
    try:
        return range(1, int(value) + 1)
    except:
        return []
