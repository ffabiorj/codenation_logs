# Generated by Django 3.0.6 on 2020-05-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20200528_1434"),
    ]

    operations = [
        migrations.AddField(
            model_name="log",
            name="event",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="log",
            name="level",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
