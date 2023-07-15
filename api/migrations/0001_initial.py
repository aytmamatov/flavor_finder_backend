# Generated by Django 4.2.3 on 2023-07-14 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
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
                ("name", models.CharField(max_length=255)),
                ("rating", models.FloatField()),
                ("address", models.CharField(max_length=255)),
                ("num_reviews", models.IntegerField()),
                ("average_price", models.IntegerField()),
                ("map_link", models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("user_name", models.CharField(max_length=255)),
                ("rating", models.FloatField()),
                ("review", models.TextField()),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="api.place",
                    ),
                ),
            ],
        ),
    ]
