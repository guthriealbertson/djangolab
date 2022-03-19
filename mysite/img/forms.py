from django import forms
from .models import *
  
class photo(forms.ModelForm):
  
    class Meta:
        model = photo
        fields = ['name', 'avatar']