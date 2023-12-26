from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .views import IndexView

app_name = "core"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
