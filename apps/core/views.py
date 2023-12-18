from typing import Any

from django.views.generic import TemplateView

from apps.user.models import User


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["counts"] = range(1, 20)
        context["user"] = User.objects.first()
        return context
