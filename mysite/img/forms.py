from django import forms
from .models import *
  
  
class photoform(forms.ModelForm):
  
    class Meta:
        model = photomodel
        fields = ['name', 'avatar', 'filtertype']