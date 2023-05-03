from django import template

register = template.Library()

@register.filter
def subtract_(value, arg):
    return int(arg) - int(value)