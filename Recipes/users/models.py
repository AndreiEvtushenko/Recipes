from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    telegram = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'email', 'telegram']

    def __str__(self):
        return self.username
