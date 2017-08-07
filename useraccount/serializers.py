from django.contrib.auth.models import User
from rest_framework import serializers

class UserProileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # def validate(self, data):
    #     print ('data', data)
    #     if User.objects.filter(email=data.email).exists():
    #         raise serializers.ValidationError('User Already Exists')