# Generated by Django 3.2.25 on 2024-08-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0011_auto_20240810_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
