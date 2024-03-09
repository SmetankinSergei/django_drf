from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from materials.models import Course, Lesson
from users.constants import PAYMENT_OPTIONS


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35)
    hometown = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='users/avatars/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    client = models.ForeignKey(to=User, on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)
    target_course = models.ForeignKey(to=Course, on_delete=CASCADE, **NULLABLE)
    target_lesson = models.ForeignKey(to=Lesson, on_delete=CASCADE, **NULLABLE)
    amount = models.PositiveIntegerField()
    payment_option = models.CharField(max_length=10, choices=PAYMENT_OPTIONS)
