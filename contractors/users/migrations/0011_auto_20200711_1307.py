# Generated by Django 3.0.8 on 2020-07-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200711_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='alumni',
            field=models.CharField(default='Yes', max_length=3),
        ),
    ]
