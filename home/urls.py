from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls'), name='blog'),
    path('admin/', admin.site.urls, name='settings'),
    
]