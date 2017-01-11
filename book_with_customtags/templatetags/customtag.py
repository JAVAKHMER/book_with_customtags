from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    return str(arg1) +" "+ str(arg2)

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter
@stringfilter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()