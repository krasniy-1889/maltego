from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Post


class PostListViews(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.prefetch_related("tags").all()

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("tags").all()
    template_name = "post/post_detail.html"
    context_object_name = "post"

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
