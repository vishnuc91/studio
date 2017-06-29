# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import listdir, path
# from os.path import isfile, join
from django.shortcuts import render, redirect
import boto3
from django.conf import settings
from .models import *
# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

    def post(self, request):
        # uploaded = UploadedFiles.objects.all()
        # onlyfiles = [path.join(settings.FILE_LOCATION, f) for f in listdir(settings.FILE_LOCATION)]
        # print filter(lambda x: x in uploaded, onlyfiles)


        s3 = boto3.client('s3')
        filename = '/home/vishnu/Pictures/pondichery/cool.jpg'
        bucket_name = 'devopsstudio'
        uploaded_data = UploadedFiles()
        uploaded_data.name = filename
        uploaded_data.path = filename
        uploaded_data.save()
        # # Uploads the given file using a managed uploader, which will split up large
        # # files automatically and upload parts in parallel.
        s3.upload_file(filename, bucket_name, filename)
        return redirect('/')
        # return render(request, 'home.html', {'foo': 'bar'}, content_type='application/xhtml+xml')
