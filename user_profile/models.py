# user_profile/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default.png')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
