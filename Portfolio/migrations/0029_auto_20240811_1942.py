# Generated by Django 3.2.25 on 2024-08-11 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0028_auto_20240811_1934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='achivements',
            new_name='achievement',
        ),
        migrations.RenameModel(
            old_name='main_head_achivement',
            new_name='main_head_achievement',
        ),
    ]
