from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  
#Create your views here
def avatarView(request):
  
    if request.method == 'POST':
        form = photo(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = photo()
    return render(request, 'studentform.html', {'form' : form})
  
  
def success(request):
    return HttpResponse(' upload successful')


def display(request):
    return HttpResponse(' display successful')