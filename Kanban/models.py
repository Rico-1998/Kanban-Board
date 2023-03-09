from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title: models.CharField(max_length=200)
    description: models.CharField(max_length=200)
    # category:


# class Category(models.Model):
