from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
# class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active", "is_staff"]
    search_fields = ["userpermission_classes = [IsAuthenticated]name", "email"]
    ordering = []
