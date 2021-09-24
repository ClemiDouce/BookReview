from django import template

register = template.Library()

@register.filter()
def range(max=1):
    return range(max)