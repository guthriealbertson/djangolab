from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
import urllib.request
# Create your models here.

class photomodel(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='media/')

    def save(self):
        im = Image.open(self.avatar)
        im.convert('RGB') # convert mode
        im.thumbnail((50, 50)) # resize image
        thumb_io = BytesIO() # create a BytesIO object
        im.save(thumb_io, 'PNG', quality=85) # save image to BytesIO object


        thumbnail = File(thumb_io, name=self.name) # 
        self.avatar = File(thumbnail, name=self.name)
        super().save()
