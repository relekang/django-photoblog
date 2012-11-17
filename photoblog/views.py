# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from photoblog.models import Photo

def index (request):
    try:
        photo = Photo.objects.filter(date_published__lte=datetime.now())[0]
    except:
        raise Http404

    return render(request, 'photoblog/index.html', {
        'photo': photo
    })