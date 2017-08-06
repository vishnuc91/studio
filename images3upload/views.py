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
        uploaded = [path.join(settings.FILE_LOCATION, upload_file.name) for upload_file in UploadedFiles.objects.all()]
        folder_files = [path.join(settings.FILE_LOCATION, f) for f in listdir(settings.FILE_LOCATION)]
        print (uploaded, folder_files)
        new_images = [v for v in folder_files if v not in uploaded]


        for image in new_images:
            # # Uploads the given file using a managed uploader, which will split up large
            # # files automatically and upload parts in parallel.
            s3 = boto3.client('s3')
            bucket_name = 'devopsstudio'
            uploaded_data = UploadedFiles()
            uploaded_data.name = image.split('/home/vishnu/Pictures/sample/')[1]
            uploaded_data.path = image
            uploaded_data.save()
            s3.upload_file(image, bucket_name, uploaded_data.name)
        else:
            print ("No new images")


        return redirect('/')
        # return render(request, 'home.html', {'foo': 'bar'}, content_type='application/xhtml+xml')
