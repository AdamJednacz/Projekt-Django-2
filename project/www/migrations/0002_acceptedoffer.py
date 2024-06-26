# Generated by Django 4.1 on 2024-05-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcceptedOffer",
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
                ("name", models.CharField(max_length=10)),
                ("surname", models.CharField(max_length=10)),
                ("mail", models.CharField(max_length=100)),
                ("number", models.CharField(max_length=12)),
                ("photo", models.ImageField(upload_to="images")),
                ("text", models.CharField(max_length=150)),
                ("accepted_at", models.DateTimeField(auto_now_add=True)),
                ("industry", models.ManyToManyField(to="www.industry")),
            ],
        ),
    ]
