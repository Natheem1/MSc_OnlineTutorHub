# Generated by Django 4.2.3 on 2023-08-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0017_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutorprofile", name="bio", field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="tutorprofile",
            name="short_intro",
            field=models.CharField(max_length=200, null=True),
        ),
    ]