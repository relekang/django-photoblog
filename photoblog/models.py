# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category (models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = 'Category'
        verbose_name = 'Categories'

class Location (models.Model):
    name = models.CharField(max_length=80, verbose_name=_('name'))

class Photo (models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    file = models.ImageField(upload_to='photoblog/', verbose_name=_('file'))
    category = models.ForeignKey(Category, related_name='photos', verbose_name=_('category'))
    location = models.ForeignKey(Location, null=True, blank=True, related_name='photos', verbose_name=_('location'))