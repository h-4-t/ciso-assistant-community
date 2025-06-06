# Generated by Django 5.1.8 on 2025-05-12 18:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("iam", "0012_user_keep_local_login"),
        ("knox", "0009_extend_authtoken_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalAccessToken",
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
                (
                    "auth_token",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.KNOX_TOKEN_MODEL,
                    ),
                ),
            ],
        ),
    ]
