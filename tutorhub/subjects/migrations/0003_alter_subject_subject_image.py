# Generated by Django 4.2.3 on 2023-08-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0002_subject_subject_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="subject_image",
            field=models.ImageField(
                blank=True,
                default="defaultprofileimg/default.png",
                null=True,
                upload_to="subject-image/",
            ),
        ),
    ]
