import os

from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker

from ...helpers import get_default_user
from ...models import Genre, Post, Tag

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with sample post data"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of posts to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]

        for _ in range(10):
            genre = Genre(name=fake.word())
            genre.save()

        for _ in range(10):
            tag = Tag(name=fake.word())
            tag.save()
        genres = Genre.objects.all()
        tags = Tag.objects.all()

        for _ in range(total):
            post = Post(
                user=get_default_user(),
                rus_name=fake.sentence(nb_words=3),
                en_name=fake.sentence(nb_words=3),
                original_name=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                issue_year=fake.date(),
                age_limit=fake.random_element(
                    elements=("ALL", "6+", "12+", "16+", "18+")
                ),
                status=Post.STATUSES._ANONS,
                likes=fake.random_int(min=0, max=100),
                views=fake.random_int(min=0, max=1000),
                count_chapters=fake.random_int(min=0, max=50),
                type=Post.TYPES._MANHWA,
                is_licensed=fake.boolean(),
                is_erotic=fake.boolean(),
            )
            post.save()
            post.genres.set(genres)
            post.tags.set(tags)

            # image_path = os.path.abspath("./pirate.jpg")
            # with open(image_path, "rb") as f:
            #     post.poster.save(f"pirate_{post.pk}.jpg", File(f), save=True)

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {total} posts"))
