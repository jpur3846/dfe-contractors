# Generated by Django 3.0.8 on 2020-07-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200713_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='tax',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='fee_incl_gst',
            field=models.IntegerField(null=True),
        ),
    ]