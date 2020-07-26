from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class cv(models.Model):
    about = models.TextField(default="null")
    work = models.TextField(default="null")
    skills = models.TextField(default="null")
    education = models.TextField(default="null")
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated = models.DateTimeField(blank=True, null=True)
