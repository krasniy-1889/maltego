from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, null=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_users"


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(max_length=800, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
