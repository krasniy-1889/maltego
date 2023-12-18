from collections.abc import Iterable

from django.db import models
from django.template.defaultfilters import slugify

from ..user.models import User


def get_default_user():
    return User.objects.filter(is_superuser=True).first()


class Status(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Type(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    img = models.URLField()
    dir = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Chapter(models.Model):
    id = models.IntegerField(primary_key=True)
    tome = models.IntegerField()
    chapter = models.CharField(max_length=255)


class Post(models.Model):
    rus_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="posters/")
    description = models.TextField()
    issue_year = models.DateField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    count_rating = models.IntegerField()
    age_limit = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    categories = models.ManyToManyField(Category)
    count_chapters = models.IntegerField()
    is_licensed = models.BooleanField()
    publishers = models.ManyToManyField(Publisher)
    is_yaoi = models.BooleanField()
    is_erotic = models.BooleanField()
