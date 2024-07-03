from django.db import models

# Create your models here.

class LOGIN(models.Model):
    user_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)