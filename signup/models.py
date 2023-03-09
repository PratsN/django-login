from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Registration(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
