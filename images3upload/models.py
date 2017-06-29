# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UploadedFiles(models.Model):
    name = models.CharField('Name of file', max_length=100)
    path = models.CharField('Path of file', max_length=100)

    def __unicode__(self):
        return self.name
