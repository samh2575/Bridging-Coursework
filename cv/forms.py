from django import forms
from cv.models import cv

class cvForm(forms.ModelForm):
    # about = forms.CharField()
    # work = forms.CharField()
    # skills = forms.CharField()
    # education = forms.CharField()

    class Meta:
        model = cv
        fields = ('about', 'work', 'skills', 'education',)
    
