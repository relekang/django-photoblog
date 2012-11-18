# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from photoblog.models import Photo

def index (request):
    try:
        photo = Photo.objects.filter(date_published__lte=datetime.now())[0]
    except:
        raise Http404

    return render(request, 'photoblog/index.html', {
        'photo': photo,
        'date_as_title': getattr(settings, 'PHOTOBLOG_DATE_AS_TITLE', False)
    })

def photo (request, id):
    photo = get_object_or_404(
        Photo.objects.prefetch_related('tags').select_related('category', 'location'),
        pk=id,
        date_published__lte=datetime.now()
    )

    return render(request, 'photoblog/index.html', {
        'photo': photo,
        'date_as_title': getattr(settings, 'PHOTOBLOG_DATE_AS_TITLE', False)
    })
