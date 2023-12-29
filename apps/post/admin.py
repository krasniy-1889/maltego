from django.contrib import admin

from .forms import ChapterPageForm
from .models import Chapter, ChapterPage, Genre, Like, Post, Tag


# * Inlines
class ChapterPageInline(admin.TabularInline):
    model = ChapterPage
    form = ChapterPageForm
    extra = 1


# * Model
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "rus_name",
        "status",
        "likes",
        "views",
        "is_licensed",
        "is_erotic",
    ]
    filter_horizontal = ["genres", "tags"]
    show_full_result_count = False


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["id", "chapter_number", "post__rus_name"]
    inlines = [ChapterPageInline]

    def post__rus_name(self, obj):
        return obj.post.rus_name


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["user__username", "post__rus_name"]
    list_select_related = ["user", "post"]
    show_full_result_count = False

    def user__username(self, obj):
        return obj.user.username

    def post__rus_name(self, obj):
        return obj.post.rus_name
