# Generated by Django 3.0.8 on 2020-07-27 10:56

from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_auto_20200727_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='total_gst_amount',
            new_name='gst_amount',
        ),
        migrations.AddField(
            model_name='event',
            name='parking_total',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='fee',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[events.validators.fee_positive_validator]),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='fee_all_incl',
            field=models.FloatField(blank=True, default=0, null=True, validators=[events.validators.fee_positive_validator]),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='gst_amnt',
            field=models.FloatField(blank=True, default=0, null=True, validators=[events.validators.fee_positive_validator]),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='inclusions',
            field=models.IntegerField(default=0, null=True, validators=[events.validators.fee_positive_validator]),
        ),
    ]