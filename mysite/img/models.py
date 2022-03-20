from django.db import models

# Create your models here.

class photomodel(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='media/')
