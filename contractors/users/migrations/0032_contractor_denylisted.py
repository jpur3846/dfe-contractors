# Generated by Django 3.0.8 on 2020-07-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_remove_contractor_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='denylisted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]