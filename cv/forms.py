from django import forms
from cv.models import cv

class cvForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = cv
        fields = ('name',)
    
