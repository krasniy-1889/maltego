from django.contrib import admin

from .models import Genre, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "likes",
        "dislikes",
        "author",
        "tag_list",
    ]
    list_select_related = ["author"]
    search_fields = [
        "title",
        "author__username",
    ]
    list_filter = [
        "created_at",
        "updated_at",
        "author",
    ]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags", "genres"]
    show_full_result_count = False

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    def genre_list(self, obj):
        return ", ".join(o.name for o in obj.genres.all())


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]
