# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password
import json

# Create your views here.
class LoginView(APIView):

     def post(self, request):
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
            # A backend authenticated the credentials
            if Token.objects.filter(user=user).exists():
                token = Token.objects.get(user=user)
            else:
                token = Token.objects.create(user=user)
            return Response({'status': 200, 'token': token.key})
         else:
            return Response({'status': 500})


class Signup(APIView):

    def post(self, request):
        print (request.data)
        user_serializer = UserProileSerializer(data=request.data)
        if user_serializer.is_valid():
            user = User()
            user.username = request.data['username']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            user.password = make_password(request.data['password2'])
            user.save()
            profile = Useraccount()
            profile.user = user
            profile.bucket_name = request.data['bucket_name']
            profile.save()
            return Response({'status': 200, 'data': user_serializer.data})
        else:
            return Response({'status': 500, 'data': user_serializer.errors})