from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    pass


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label="Логин",
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={"class": "form-control", "placeholder": "Логин..."}
#         ),
#         strip=True,
#         required=True,
#     )
#     password = forms.CharField(
#         label="Пароль",
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Пароль..."}
#         ),
#         strip=True,
#         required=True,
#     )
