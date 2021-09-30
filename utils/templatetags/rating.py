from django import template

register = template.Library()


@register.filter()
def vrange(min, max=0):
    if max == 0:
        return range(min)
    else:
        return range(min, max)
