from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class PollingUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)