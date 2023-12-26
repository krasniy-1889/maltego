from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path("", include("apps.core.urls", namespace="core")),
    path("", include("apps.user.urls", namespace="user")),
    path("", include("apps.post.urls", namespace="post")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
