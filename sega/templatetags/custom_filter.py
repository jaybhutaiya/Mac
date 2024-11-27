from django import template

register = template.Library()

@register.filter()
def block(value):
    return value.split('$')
