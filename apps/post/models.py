from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from .helpers import chapter_page_upload_to


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
    class AGE_LIMIT(models.TextChoices):
        _ALL = "all", "All"
        _6 = "6+", "6+"
        _12 = "12+", "12+"
        _16 = "16+", "16+"
        _18 = "18+", "18+"

    class STATUSES(models.TextChoices):
        _DRAFT = "черновик", "Черновик"
        _PUBLISHED = "опубликовано", "Опибликовано"
        _FROZED = "заморожено", "Заморожено"
        _ANONS = "анонс", "Анонс"

    class TYPES(models.TextChoices):
        _MANGA = "манга", "Манга"
        _MANHWA = "манхва", "Манхва"
        _MANHUA = "маньхуа", "Маньхуа"
        _WESTERN_COMICS = "западный комикс", "Западный комикс"
        _WEBTOON = "рукомикс", "Рукомикс"
        _INDONESIAN_COMICS = "индонезийский комикс", "Индонезийский комикс"
        _OTHER = "другое", "Другое"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rus_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/")
    issue_year = models.DateField()
    age_limit = models.CharField(max_length=7, choices=AGE_LIMIT.choices)
    status = models.CharField(max_length=20, choices=STATUSES.choices)
    type = models.CharField(max_length=20, choices=TYPES.choices)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    count_chapters = models.PositiveIntegerField(default=0)
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
