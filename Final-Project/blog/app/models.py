from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(blank=True)
    content = models.CharField(max_length=100000)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return self.email