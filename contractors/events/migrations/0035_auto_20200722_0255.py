# Generated by Django 3.0.8 on 2020-07-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_auto_20200722_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]