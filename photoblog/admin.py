from django.contrib import admin
from photoblog.models import Category, Location, Photo, Tag


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'number_of_photos')

class LocationAdmin (admin.ModelAdmin):
    list_display = ('name', 'number_of_photos')

class PhotoAdmin (admin.ModelAdmin):
    list_display = (
        'thumb_small_as_html',
        'title',
        'date_published',
        'category',
        'location',
        'list_of_tags',
        'description_as_meta_tag_only',
        )
    list_filter = ('category', 'location', 'tags')
    date_hierarchy = 'date_published'

class TagAdmin (admin.ModelAdmin):
    list_display = ('title', 'number_of_photos')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)