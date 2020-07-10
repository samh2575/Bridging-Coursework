from django.views.generic import TemplateView
from cv.forms import cvForm
from cv.models import cv
from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.

def cv_view(request):
    content = cv.objects.order_by('-updated')[:1]
    return render(request, 'cv/cv.html', {'content' : content})

def cv_edit(request):
    form = cvForm()  
    if request.method == "POST":
        form = cvForm(request.POST, request.user)
        if form.is_valid():
            new = form.save(commit=False)
            new.auther = request.user
            new.updated = timezone.now()
            new.save()
            return redirect('/cv/')

        return render(request, 'cv/cv_edit.html', {'form': form})
    else:
        content = cv.objects.order_by('-updated')[:1]
        form = cvForm(instance=content[0])
        return render(request, 'cv/cv_edit.html', {'form': form})
