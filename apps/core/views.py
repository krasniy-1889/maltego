from typing import Any

from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["counts"] = range(1, 20)
        context["user"] = get_user_model().objects.first()
        return context
