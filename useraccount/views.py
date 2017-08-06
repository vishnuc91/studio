# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class LoginView(APIView):

     def post(self, request):
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
            # A backend authenticated the credentials
            token = Token.objects.create(user=user)
            return Response({'status': 200, 'token': token.key})
         else:
            return Response({'status': 500})


class Signup(APIView):

    def post(self, request):
        return Response({'status': ok})