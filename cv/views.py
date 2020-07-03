from django.shortcuts import render
from django.views.generic import TemplateView
from cv.forms import cvForm
# Create your views here.

def cv(request):
    return render(request, 'cv/cv.html', {})

class cv_edit(TemplateView):
    template_name = 'cv/cv_edit.html'

    def get(self, request):
        form = cvForm()
        return render(request, self.template_name, {'form': form})