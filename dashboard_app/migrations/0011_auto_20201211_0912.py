# Generated by Django 3.1.3 on 2020-12-11 09:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0010_auto_20201211_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banklist',
            name='interest',
            field=models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
