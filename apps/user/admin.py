from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import UserProfile


@admin.register(get_user_model())
# class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active", "is_staff"]
    search_fields = ["userpermission_classes = [IsAuthenticated]name", "email"]
    ordering = []


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ["id", "user", "bio"]
