# Generated by Django 3.0.8 on 2020-07-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_remove_event_bandleader'),
        ('users', '0029_auto_20200715_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='events',
            field=models.ManyToManyField(to='events.Event'),
        ),
    ]