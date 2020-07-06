from django.views.generic import TemplateView
from cv.forms import cvForm
from django.shortcuts import render, redirect

# Create your views here.

def cv(request):
    return render(request, 'cv/cv.html', {})

def cv_edit(request):

    if request.method == "POST":
        form = cvForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()

            text = form.cleaned_data['name']
            return redirect('cv')
    
        args = {'form': form, 'text': text}
        return render(request, 'cv/cv_edit.html', args)
    else:
        form = cvForm()
        return render(request, 'cv/cv_edit.html', {'form': form})
