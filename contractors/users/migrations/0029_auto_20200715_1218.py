# Generated by Django 3.0.8 on 2020-07-15 12:18

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20200714_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='abn',
            field=models.IntegerField(blank=True, null=True, validators=[users.validators.abn_validator]),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='gst_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
