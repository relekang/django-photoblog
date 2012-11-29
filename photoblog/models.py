# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.templatetags.thumbnail import is_portrait
from photoblog.util import expire_page_cache

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

    def number_of_photos(self):
        return self.photos.all().count()

class Location (models.Model):
    name = models.CharField(max_length=80, verbose_name=_('name'))

    def __unicode__(self):
        return self.name

    def number_of_photos(self):
        return self.photos.all().count()

class Tag (models.Model):
    title = models.CharField(max_length=80, verbose_name=_('name'))

    def __unicode__(self):
        return self.title

    def number_of_photos(self):
        return self.photos.all().count()

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

    class Meta:
        ordering = ('-date_published',)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        expire_page_cache('photoblog_view_photo', args=[self.pk])

    def thumb(self, geometry_string, crop=None):
        thumb = get_thumbnail(self.file, geometry_string, crop=crop)
        return thumb

    def thumb_big(self):
        if is_portrait(self.file):
            return self.thumb(geometry_string='x800')
        else:
            return self.thumb(geometry_string='800')

    def thumb_medium(self):
        if is_portrait(self.file):
            return self.thumb(geometry_string='x400')
        else:
            return self.thumb(geometry_string='400')

    def thumb_small(self):
        return self.thumb(geometry_string='200x200', crop='center')

    def thumb_small_as_html(self):
        return mark_safe('<img src="%s">' % self.thumb_small().url)
    thumb_small_as_html.allow_tags = True
    thumb_small_as_html.short_description = 'image'

    def exif(self):
        exif_data = cache.get(self.exif_cache_key())
        if exif_data is None:
            data = {}
            try:
                photo = Image.open(self.file)
                info = photo._getexif()
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    data[decoded] = value

                cache.set(self.exif_cache_key(), data)
                exif_data = data
            except:
                exif_data = None

        return exif_data

    def exif_cache_key(self):
        return "exif%s" % self.pk

    def list_of_tags(self):
        return ', '.join([tag.title for tag in self.tags.all()])
