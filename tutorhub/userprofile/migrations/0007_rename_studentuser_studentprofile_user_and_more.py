# Generated by Django 4.2.3 on 2023-08-09 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0006_alter_studentprofile_profile_image_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentprofile", old_name="studentuser", new_name="user",
        ),
        migrations.RenameField(
            model_name="tutorprofile", old_name="tutoruser", new_name="user",
        ),
    ]
