# Generated by Django 3.0.8 on 2020-07-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20200722_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
