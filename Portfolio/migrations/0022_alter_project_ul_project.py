# Generated by Django 3.2.25 on 2024-08-11 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0021_main_head_project_project_project_ul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_ul',
            name='Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='Portfolio.project'),
        ),
    ]
