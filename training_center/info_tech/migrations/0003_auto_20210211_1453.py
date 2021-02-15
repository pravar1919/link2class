# Generated by Django 2.2 on 2021-02-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_tech', '0002_auto_20210211_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infotech',
            options={'verbose_name_plural': 'InfoTech_Videos'},
        ),
        migrations.AlterField(
            model_name='infotech',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='infotech',
            name='length',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='infotech',
            name='todays_events',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='infotech',
            name='views',
            field=models.IntegerField(blank=True),
        ),
    ]