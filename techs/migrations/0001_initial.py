# Generated by Django 4.1.7 on 2023-06-11 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tech",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Iniciante", "Beginner"),
                            ("Intermediário", "Intermediate"),
                            ("Avançado", "Advanced"),
                        ],
                        default="Iniciante",
                        max_length=256,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date of creation"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date of last modification"
                    ),
                ),
            ],
        ),
    ]
