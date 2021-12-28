#post_reverse_filter
from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg