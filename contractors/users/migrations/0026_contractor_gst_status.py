# Generated by Django 3.0.8 on 2020-07-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200713_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='gst_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True),
        ),
    ]
