# Generated by Django 2.2 on 2021-02-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='todays_events',
            field=models.URLField(),
        ),
    ]
