# -*- coding: UTF-8 -*-
from django.template import Library

register = Library()

@register.filter
def format_exif_date(value, arg=None):
    date = value.split(' ')[0].split(':')
    return "%s.%s.%s" % (date[2], date[1], date[0])