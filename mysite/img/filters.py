from io import BytesIO
from django.core.files import File
from PIL import Image, ImageOps,ImageFilter

def blur(image):
    im = Image.open(image.avatar)
    im = im.filter(ImageFilter.BoxBlur(radius=10))
    byte = BytesIO() 
    im.save(byte, 'PNG', quality=85) 
    temp = File(byte, name=image.name) 
    return temp

def gray(image):
    im = Image.open(image.avatar)
    im = ImageOps.grayscale(im)
    byte = BytesIO()
    im.save(byte, 'PNG', quality=85)
    temp = File(byte, name=image.name) 
    return temp

def poster(image):
    im = Image.open(image.avatar)
    im = ImageOps.posterize(im,3)
    byte = BytesIO() 
    im.save(byte, 'PNG', quality=85) 
    temp = File(byte, name=image.name) 
    return temp