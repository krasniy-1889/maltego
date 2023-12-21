from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("apps.core.urls")),
    path("", include("apps.user.urls")),
    path("admin/", admin.site.urls),
]
