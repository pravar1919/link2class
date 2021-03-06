# Generated by Django 2.2 on 2021-02-19 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Peer2Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_field', models.CharField(default='peer2peer', max_length=220)),
                ('title', models.CharField(max_length=500)),
                ('todays_events', models.URLField(blank=True, null=True)),
                ('upcoming_events', models.URLField(blank=True, null=True)),
                ('ondemand_events', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('certificate', models.CharField(blank=True, max_length=220, null=True)),
                ('Audience', models.CharField(blank=True, max_length=220, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Peer2Peer',
            },
        ),
    ]
