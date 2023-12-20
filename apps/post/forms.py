from django import forms

from .models import ChapterPage


# * Admin
class ChapterPageForm(forms.ModelForm):
    class Meta:
        model = ChapterPage
        fields = ["image", "post"]


# * User
