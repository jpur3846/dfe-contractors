# Generated by Django 3.0.8 on 2020-07-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200713_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
