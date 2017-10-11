# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def upload_img(request):
    print(request.POST)
    if request.method == 'POST':
        try:
            img = request.FILES.get('img')
            f = open(img.name, 'wb')
            for chunk in img.chunks(chunk_size=1024):
                f.write(chunk)
        except Exception as e:
            print e
        finally:
            f.close()
    return HttpResponse('ok')
    
