from allauth.account.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm


# Create your views here.
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "user/auth/modal/login.html"
    success_url = reverse_lazy("core:home")
