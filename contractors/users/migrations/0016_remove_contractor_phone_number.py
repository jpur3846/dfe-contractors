# Generated by Django 3.0.8 on 2020-07-11 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200711_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='phone_number',
        ),
    ]