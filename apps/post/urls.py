from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListViews.as_view(), name="list"),
    # path("", views.PostDetailView.as_view(), name="detail"),
]
