# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('photoblog.views',
    url(r'^$', 'index', name='photoblog_index'),
    url(r'^(?P<id>\d+)/$', 'photo', name='photoblog_view_photo'),
)