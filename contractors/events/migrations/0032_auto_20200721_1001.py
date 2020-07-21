# Generated by Django 3.0.8 on 2020-07-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0031_auto_20200719_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmusicians',
            name='feedback_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='No', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='instrument',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='invoice_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='No', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='is_bandleader',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='eventmusicians',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='No', max_length=3, null=True),
        ),
    ]