# Generated by Django 3.2.25 on 2024-08-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0023_alter_main_head_project_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_head_project',
            name='Title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
