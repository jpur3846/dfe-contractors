# Generated by Django 3.0.8 on 2020-07-30 06:15

from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0043_auto_20200729_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='card_type',
            field=models.CharField(blank=True, choices=[('domestic', 'Domestic'), ('international', 'International')], default='domestic', max_length=30, null=True, validators=[events.validators.card_validator]),
        ),
    ]
