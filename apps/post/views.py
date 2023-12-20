from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Post


class PostListViews(ListView):
    model = Post
    queryset = (
        Post.objects.select_related(
            "status",
            "type",
        )
        .prefetch_related(
            "tags",
            "genres",
        )
        .all()
    )
    template_name = "post/list.html"
    context_object_name = "posts"
    paginate_by = 20

    # @method_decorator(cache_page(60 * 15))
    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.select_related("author").prefetch_related(
        "tags",
        "genres",
    )
    template_name = "post/detail.html"
    context_object_name = "post"
