# Generated by Django 5.0 on 2023-12-21 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("post", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="genres",
            field=models.ManyToManyField(related_name="genres", to="post.genre"),
        ),
        migrations.AddField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="chapterpage",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.status"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="tags", to="post.tag"),
        ),
        migrations.AddField(
            model_name="post",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="post.type"
            ),
        ),
    ]
