from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path("manga/", views.PostListView.as_view(), name="list"),
    path("manga/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]
