from django.db import models
from django.core.files import File
from .filters import *

# Create your models here.

class photomodel(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    filtertype = models.CharField(max_length=50)
    
    def save(self):
        self.name += '.png'

        if self.filtertype == 'blur':
            temp = blur(self)
            self.photo = File(temp, self.name)
        if self.filtertype == 'gray':
            temp = gray(self)
            self.photo = File(temp, self.name)
        if self.filtertype == 'poster':
            temp = poster(self)
            self.photo = File(temp, self.name)
        
        super().save()
