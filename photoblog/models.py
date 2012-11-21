# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail

try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    import Image
    from ExifTags import TAGS



class Category (models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Location (models.Model):
    name = models.CharField(max_length=80, verbose_name=_('name'))

    def __unicode__(self):
        return self.name

class Tag (models.Model):
    title = models.CharField(max_length=80, verbose_name=_('name'))

    def __unicode__(self):
        return self.title

class Photo (models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name=_('title'))
    date_uploaded = models.DateField(editable=False, auto_now_add=True)
    date_published = models.DateTimeField(verbose_name=_('publish date'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    description_as_meta_tag_only = models.BooleanField(default=True, verbose_name=_('view description only as meta-tag'))
    file = models.ImageField(upload_to='photoblog/', verbose_name=_('file'))
    category = models.ForeignKey(Category, null=True, blank=True, related_name='photos', verbose_name=_('category'))
    location = models.ForeignKey(Location, null=True, blank=True, related_name='photos', verbose_name=_('location'))
    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='photos', verbose_name=_('tags'))

    def thumb(self, geometry_string, crop=None):
        thumb = get_thumbnail(self.file, geometry_string, crop=crop)
        return thumb

    def thumb_big(self):
        return self.thumb(geometry_string='800')

    def thumb_medium(self):
        return self.thumb(geometry_string='400')

    def thumb_small(self):
        return self.thumb(geometry_string='150x150', crop='center')

    def exif(self):
        exif_data = cache.get(self.exif_cache_key())
        if exif_data is None:
            data = {}
            photo = Image.open(self.file)
            info = photo._getexif()
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                data[decoded] = value

            cache.set(self.exif_cache_key(), data)
            exif_data = data

        return exif_data

    def exif_cache_key(self):
        return "exif%s" % self.pk
