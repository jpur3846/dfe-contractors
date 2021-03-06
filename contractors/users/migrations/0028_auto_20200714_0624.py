# Generated by Django 3.0.8 on 2020-07-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20200713_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='meal_preference',
            field=models.CharField(blank=True, choices=[('standard', 'Standard'), ('vegetarian', 'Vegetarian'), ('vegan', 'Vegan'), ('pescetarian', 'Pescetarian'), ('gluten_free', 'Gluten Free'), ('halal', 'Halal'), ('kosher', 'Kosher'), ('dairy_free', 'Dairy Free')], default='standard', max_length=50, null=True),
        ),
    ]
