from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class cv(models.Model):
    about = models.TextField()
    work = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated = models.DateTimeField(blank=True, null=True)
