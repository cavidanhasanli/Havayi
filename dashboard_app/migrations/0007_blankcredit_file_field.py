# Generated by Django 3.1.3 on 2020-12-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0006_auto_20201203_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='blankcredit',
            name='file_field',
            field=models.FileField(blank=True, null=True, upload_to='user_files'),
        ),
    ]