# Generated by Django 4.1 on 2024-05-18 18:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0010_rename_comment_like_acceptedoffer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="acceptedoffer",
            new_name="accepted_offer",
        ),
        migrations.RenameField(
            model_name="unlike",
            old_name="acceptedoffer",
            new_name="accepted_offer",
        ),
    ]
