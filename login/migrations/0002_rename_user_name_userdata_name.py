# Generated by Django 4.1.7 on 2024-11-14 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userdata",
            old_name="user_name",
            new_name="name",
        ),
    ]
