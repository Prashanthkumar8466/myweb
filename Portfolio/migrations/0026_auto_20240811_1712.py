# Generated by Django 3.2.25 on 2024-08-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0025_auto_20240811_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_head_project',
            name='desk_image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='main_head_project',
            name='moble_image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
