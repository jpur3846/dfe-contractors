# Generated by Django 3.0.8 on 2020-07-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_eventmusicians_email_invite_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='email_worksheet_reminder',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]