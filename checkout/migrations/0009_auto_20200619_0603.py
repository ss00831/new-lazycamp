# Generated by Django 3.0.6 on 2020-06-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20200520_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='booking_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='number_nights',
            field=models.IntegerField(null=True),
        ),
    ]
