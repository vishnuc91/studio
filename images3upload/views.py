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
        uploaded = [upload_file.name for upload_file in UploadedFiles.objects.all()]
        folder_files = [path.join(settings.FILE_LOCATION, f) for f in listdir(settings.FILE_LOCATION)]
        print [i for i, j in zip(folder_files, uploaded) if i == j]
        print uploaded, folder_files
        for file_name in folder_files:
            if file_name in uploaded:
                print 'inside if', file_name.name
            else:
                print "inside else"
                # # Uploads the given file using a managed uploader, which will split up large
                # # files automatically and upload parts in parallel.
                s3 = boto3.client('s3')
                bucket_name = 'devopsstudio'
                uploaded_data = UploadedFiles()
                uploaded_data.name = file_name.split('/home/vishnu/Pictures/sample/')[1]
                uploaded_data.path = file_name
                uploaded_data.save()
                s3.upload_file(file_name, bucket_name, uploaded_data.name)


        return redirect('/')
        # return render(request, 'home.html', {'foo': 'bar'}, content_type='application/xhtml+xml')
