from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35)
    hometown = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='users/avatars/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
