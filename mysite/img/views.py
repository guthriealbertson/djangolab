from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from PIL import Image, ImageOps,ImageFilter
  
#Create your views here
def avatarView(request):
  
    if request.method == 'POST':
        form = photoform(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = photoform()
    return render(request, 'studentform.html', {'form' : form})
  
  
def success(request):
    return HttpResponse(' upload successful')


def display(request):
    if request.method == 'GET':
        Hotels = photomodel.objects.all() 
        return render(request, 'image_display.html', {'hotel_images' : Hotels})