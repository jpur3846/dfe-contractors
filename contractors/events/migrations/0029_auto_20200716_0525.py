# Generated by Django 3.0.8 on 2020-07-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_remove_contractor_events'),
        ('events', '0028_auto_20200716_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='musicians',
        ),
        migrations.AddField(
            model_name='event',
            name='musicians',
            field=models.ManyToManyField(through='events.EventMusicians', to='users.Contractor'),
        ),
    ]
