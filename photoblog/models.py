# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail


class Category (models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = 'Category'
        verbose_name = 'Categories'

class Location (models.Model):
    name = models.CharField(max_length=80, verbose_name=_('name'))

class Photo (models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    date_uploaded = models.DateField(editable=False, auto_now_add=True)
    date_published = models.DateTimeField(verbose_name=_('publish date'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    file = models.ImageField(upload_to='photoblog/', verbose_name=_('file'))
    category = models.ForeignKey(Category, related_name='photos', verbose_name=_('category'))
    location = models.ForeignKey(Location, null=True, blank=True, related_name='photos', verbose_name=_('location'))

    def thumb(self, geometry_string, crop=None):
        thumb = get_thumbnail(self.file, geometry_string, crop=crop)
        return thumb

    def thumb_big(self):
        return self.thumb(geometry_string='800')

    def thumb_medium(self):
        return self.thumb(geometry_string='400')

    def thumb_small(self):
        return self.thumb(geometry_string='150x150', crop='center')
