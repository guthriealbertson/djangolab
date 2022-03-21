from io import BytesIO
from django.core.files import File
from PIL import Image, ImageOps,ImageFilter

def blur(image):
    im = Image.open(image.avatar)
    im = im.filter(ImageFilter.BoxBlur(radius=10))
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'PNG', quality=85) # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name) # 
    return thumbnail

def gray(image):
    im = Image.open(image.avatar)
    im = ImageOps.grayscale(im)
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'PNG', quality=85) # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name) # 
    return thumbnail

def poster(image):
    im = Image.open(image.avatar)
    im = ImageOps.posterize(im,3)
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'PNG', quality=85) # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name) # 
    return thumbnail