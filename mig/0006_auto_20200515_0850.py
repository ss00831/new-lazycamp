# Generated by Django 3.0.6 on 2020-05-15 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200515_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='quantities',
            new_name='quantity',
        ),
    ]
