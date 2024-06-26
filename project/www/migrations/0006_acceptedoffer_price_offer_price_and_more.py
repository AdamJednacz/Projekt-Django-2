# Generated by Django 4.1 on 2024-05-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0005_acceptedoffer_industry"),
    ]

    operations = [
        migrations.AddField(
            model_name="acceptedoffer",
            name="price",
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="offer",
            name="price",
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="mail",
            field=models.EmailField(max_length=254, verbose_name=100),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="name",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="number",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="surname",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="offer",
            name="name",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="offer",
            name="surname",
            field=models.CharField(max_length=15),
        ),
    ]
