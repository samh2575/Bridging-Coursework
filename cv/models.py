from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class cv(models.Model):
    about = models.TextField()
    work = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(blank=True, null=True)
