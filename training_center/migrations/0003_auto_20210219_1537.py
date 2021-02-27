# Generated by Django 2.2 on 2021-02-19 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training_center', '0002_auto_20210219_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentmessage',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sentmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to=settings.AUTH_USER_MODEL),
        ),
    ]