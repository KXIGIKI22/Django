from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
