from django.urls import include, path

from . import views

app_name = "user"
urlpatterns = [
    path("accounts/", include("allauth.urls")),
    # path("accounts/login/", views.CustomLoginView.as_view(), name="login"),
]
