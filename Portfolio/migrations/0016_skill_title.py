# Generated by Django 3.2.25 on 2024-08-10 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0015_skill_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Portfolio.skill_title'),
            preserve_default=False,
        ),
    ]
