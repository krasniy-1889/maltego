from django.conf import settings
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("manga/", views.PostListView.as_view(), name="list"),
    # path("", views.PostDetailView.as_view(), name="detail"),
]
