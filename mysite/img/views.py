from django.shortcuts import render, redirect
from .forms import *
  
#Create your views here
def avatarView(request):
  
    if request.method == 'POST':
        form = photoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = photoform()
    return render(request, 'up.html', {'form' : form})
  
def display(request):
    if request.method == 'GET':
        Pics = photomodel.objects.all() 
        return render(request, 'image_display.html', {'images' : Pics})