import os
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Post, Status, Type, Genre, Tag

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
            status = Status(name=fake.word())
            status.save()

        for _ in range(10):
            type = Type(name=fake.word())
            type.save()

        for _ in range(10):
            genre = Genre(name=fake.word())
            genre.save()

        for _ in range(10):
            tag = Tag(name=fake.word())
            tag.save()

        statuses = Status.objects.all()
        types = Type.objects.all()
        genres = Genre.objects.all()
        tags = Tag.objects.all()

        for _ in range(total):
            post = Post(
                rus_name=fake.sentence(nb_words=3),
                en_name=fake.sentence(nb_words=3),
                original_name=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                issue_year=fake.date(),
                age_limit=fake.random_element(
                    elements=("ALL", "6+", "12+", "16+", "18+")
                ),
                status=fake.random_element(elements=statuses),
                likes=fake.random_int(min=0, max=100),
                views=fake.random_int(min=0, max=1000),
                count_chapters=fake.random_int(min=0, max=50),
                type=fake.random_element(elements=types),
                is_licensed=fake.boolean(),
                is_erotic=fake.boolean(),
            )
            post.save()
            post.genres.set(genres)
            post.tags.set(tags)

            image_path = os.path.abspath("./pirate.jpg")
            with open(image_path, "rb") as f:
                post.poster.save(f"pirate_{post.pk}.jpg", File(f), save=True)

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {total} posts"))
