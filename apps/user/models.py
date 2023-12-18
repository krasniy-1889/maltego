from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username
