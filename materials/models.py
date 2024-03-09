from django.db import models
from django.db.models import CASCADE


NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=250)
    preview = models.ImageField(upload_to='courses/previews/', **NULLABLE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=250)
    preview = models.ImageField(upload_to='lessons/previews/')
    description = models.TextField()
    video_url = models.URLField()
    course = models.ForeignKey(to=Course, on_delete=CASCADE, related_name='lessons')

    def __str__(self):
        return self.name
