from django.db import models
from django.core.files import File
from .filters import *


# Create your models here.

class photomodel(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField()
    filtertype = models.CharField(max_length=50)
    
    def save(self):
        
        if self.filtertype == 'blur':
            thumbnail = blur(self)
            self.avatar = File(thumbnail, self.name)
        if self.filtertype == 'gray':
            thumbnail = gray(self)
            self.avatar = File(thumbnail, self.name)
        if self.filtertype == 'poster':
            thumbnail = poster(self)
            self.avatar = File(thumbnail, self.name)
        
        super().save()
