# Generated by Django 4.2.3 on 2023-08-09 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                ("subject_name", models.CharField(max_length=60, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeachingLevel",
            fields=[
                ("teaching_level", models.CharField(max_length=60, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TutorProfile",
            fields=[
                ("username", models.CharField(blank=True, max_length=100, null=True)),
                ("first_name", models.CharField(blank=True, max_length=300, null=True)),
                ("last_name", models.CharField(blank=True, max_length=300, null=True)),
                ("location", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "short_intro",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("hourly_rate", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="profiles/default.png",
                        null=True,
                        upload_to="profiles/",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "email",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentProfile",
            fields=[
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                ("first_name", models.CharField(blank=True, max_length=300, null=True)),
                ("last_name", models.CharField(blank=True, max_length=300, null=True)),
                ("short_goal", models.CharField(blank=True, max_length=200, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("Year 7", "Year 7 KS3"),
                            ("Year 8", "Year 8 KS3"),
                            ("Year 9", "Year 9 KS3"),
                            ("Year 10", "Year 10 KS4"),
                            ("Year 11", "Year 11 KS4"),
                            ("Year 12", "Year 12 KS5"),
                            ("Year 13", "Year 13 KS5"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="profiles/default.png",
                        null=True,
                        upload_to="profiles/",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "parent_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "parent_email",
                    models.EmailField(blank=True, max_length=500, null=True),
                ),
                (
                    "parent_phone",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "preferred_availability",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Weekday mornings", "Weekday mornings"),
                            ("Weekday afternoons", "Weekday afternoons"),
                            ("Weekday evenings", "Weekday evenings"),
                            ("Weekends mornings", "Weekends mornings"),
                            ("Weekends afternoons", "Weekends afternoons"),
                            ("Weekends evenings", "Weekends evenings"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "email",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]