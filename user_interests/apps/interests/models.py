from __future__ import unicode_literals
from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length = 45)

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    interests = models.ManyToManyField(Interest)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
