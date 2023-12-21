from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_users"
