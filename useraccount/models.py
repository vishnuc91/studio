from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Useraccount(models.Model):
    user = models.ForeignKey(User, related_name='user_account')
    bucket_name = models.CharField('Bucket Name', max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User Account'
        ordering = ('created',)
