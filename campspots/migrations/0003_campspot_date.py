# Generated by Django 3.0.6 on 2020-07-29 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campspots', '0002_auto_20200721_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='campspot',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
