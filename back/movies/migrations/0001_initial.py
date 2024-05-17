# Generated by Django 4.2.13 on 2024-05-17 08:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                ("actor_code", models.IntegerField(primary_key=True, serialize=False)),
                ("actor_name", models.TextField()),
                ("profile_path", models.TextField(null=True)),
                ("popularity", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "director_code",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("director_name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("genre_code", models.IntegerField(primary_key=True, serialize=False)),
                ("genre_name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("code", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=40)),
                ("score", models.FloatField()),
                ("overview", models.TextField()),
                ("popularity", models.FloatField()),
                ("poster_url", models.TextField()),
                ("release_date", models.DateField()),
                ("actors", models.ManyToManyField(to="movies.actor")),
                ("directors", models.ManyToManyField(to="movies.director")),
                ("genres", models.ManyToManyField(to="movies.genre")),
            ],
        ),
        migrations.CreateModel(
            name="UserRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovieComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=50)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
