# Generated by Django 3.0.8 on 2020-07-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_contractor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='main_instrument',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
