# Generated by Django 4.1 on 2024-05-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0002_acceptedoffer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acceptedoffer",
            name="accepted_at",
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="mail",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="number",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="photo",
            field=models.ImageField(upload_to="photos/"),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="surname",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="acceptedoffer",
            name="text",
            field=models.TextField(),
        ),
    ]
