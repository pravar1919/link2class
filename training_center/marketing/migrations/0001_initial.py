# Generated by Django 2.2 on 2021-02-11 04:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('todays_events', models.URLField(blank=True)),
                ('upcoming_events', models.URLField(blank=True)),
                ('ondemand_events', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('certificate', models.CharField(max_length=220)),
                ('Audience', models.CharField(max_length=220)),
                ('length', models.IntegerField()),
                ('views', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
