from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("manga/", include("apps.post.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
