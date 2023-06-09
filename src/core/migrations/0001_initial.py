# Generated by Django 4.1.3 on 2023-06-05 23:45

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                    "name",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        validators=[core.utils.validate_tag_name],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Link",
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
                ("dt", models.DateTimeField(auto_now_add=True)),
                ("location", models.URLField()),
                ("domain", models.CharField(editable=False, max_length=200)),
                ("title", models.CharField(blank=True, max_length=200)),
                (
                    "owner",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="core.tag")),
            ],
            options={
                "ordering": ["-dt"],
            },
        ),
    ]
