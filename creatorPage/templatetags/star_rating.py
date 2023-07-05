from django import template

register = template.Library()


@register.filter
def subtract_(value: int, arg: int) -> int:
    return int(arg) - int(value)
