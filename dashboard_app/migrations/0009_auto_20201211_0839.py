# Generated by Django 3.1.3 on 2020-12-11 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0008_auto_20201211_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditTypeInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.RemoveField(
            model_name='banklist',
            name='credit_type',
        ),
    ]
