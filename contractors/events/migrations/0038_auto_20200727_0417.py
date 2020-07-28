# Generated by Django 3.0.8 on 2020-07-27 04:17

from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_eventmusicians_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmusicians',
            name='inclusions',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, validators=[events.validators.date_validator]),
        ),
        migrations.AlterField(
            model_name='event',
            name='unavailable_musicians',
            field=models.TextField(blank=True, default=',', null=True),
        ),
    ]