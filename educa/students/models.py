from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings


class SimpleUser(AbstractUser):
    userImg = models.ImageField(upload_to='user_avas/', default='NULL')
    group = models.CharField(max_length=200)

    def __str__(self):
        return self.username
