from django.db import models
from django.contrib.auth.models import User


class cv(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)