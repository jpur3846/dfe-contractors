# Generated by Django 3.0.8 on 2020-07-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_contractor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]