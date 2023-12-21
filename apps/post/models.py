from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from .helpers import chapter_page_upload_to


class Status(models.Model):
    """Статус манги - [Заморожен, Продолжается, Анонс, прочее....]"""

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class Type(models.Model):
    """Тип манги - [Манга, Манхва, Маньхуа, прочее....]"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанр манги"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Тэг манги"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    AGE_ALL = "ALL"
    AGE_6 = "6+"
    AGE_12 = "12+"
    AGE_16 = "16+"
    AGE_18 = "18+"

    AGE_LIMIT = (
        (AGE_ALL, "All"),
        (AGE_6, "6+"),
        (AGE_12, "12+"),
        (AGE_16, "16+"),
        (AGE_18, "18+"),
    )

    rus_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/")
    issue_year = models.DateField()
    age_limit = models.CharField(max_length=7, choices=AGE_LIMIT)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    count_chapters = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name="genres")
    tags = models.ManyToManyField(Tag, related_name="tags")
    is_licensed = models.BooleanField(default=False)
    is_erotic = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.en_name:
            self.slug = slugify(self.en_name)
        else:
            self.slug = slugify(self.original_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.rus_name


class Chapter(models.Model):
    """Глава манги"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    chapter_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        # return f"{self.chapter_count} | {self.post.rus_name}"
        return str(self.chapter_number)


class ChapterPage(models.Model):
    """Страница главы"""

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=chapter_page_upload_to)

    def __str__(self):
        return str(self.chapter.chapter_number)


class Like(models.Model):
    """Модель лайков"""

    # TODO: добавить логику дизлайков
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} | {self.post.rus_name}"
