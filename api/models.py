# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=10)
    info = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    date = models.DateTimeField('date published')