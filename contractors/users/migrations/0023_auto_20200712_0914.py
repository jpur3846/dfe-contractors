# Generated by Django 3.0.8 on 2020-07-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200712_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='profile_picture',
            field=models.ImageField(blank=True, default='generic-user.jpg', null=True, upload_to='imgs'),
        ),
    ]