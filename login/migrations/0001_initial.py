# Generated by Django 4.1.7 on 2024-11-14 08:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserData",
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
                ("user_name", models.CharField(max_length=30)),
                (
                    "password",
                    models.CharField(
                        max_length=30,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
            ],
        ),
    ]
