from django.views.generic import DetailView, ListView

from .models import Post


class PostListViews(ListView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "tags",
        "genres",
    ).all()
    template_name = "post/list.html"
    context_object_name = "posts"
    paginate_by = 20


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.select_related("author").prefetch_related(
        "tags",
        "genres",
    )
    template_name = "post/detail.html"
    context_object_name = "post"
