# Generated by Django 3.0.8 on 2020-07-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200711_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='alumni',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='battery_amp',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='pa_system',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='public_liability',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='year_finished',
        ),
    ]
