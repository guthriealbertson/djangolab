from django.db import models

# Create your models here.

class photo(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='media/')

def __str__(self):
     return self.title