# Generated by Django 4.2.3 on 2023-08-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0018_alter_tutorprofile_bio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainsubjskill",
            name="subject_name",
            field=models.CharField(max_length=200),
        ),
    ]