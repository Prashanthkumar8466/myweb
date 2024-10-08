# Generated by Django 3.2.25 on 2024-08-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='desktop_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='desktop')),
                ('image2', models.ImageField(upload_to='desktop')),
                ('image3', models.ImageField(upload_to='desktop')),
            ],
        ),
        migrations.CreateModel(
            name='greeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='home_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='home_pgh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mobile_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='mobile')),
                ('image2', models.ImageField(upload_to='mobile')),
                ('image3', models.ImageField(upload_to='mobile')),
            ],
        ),
    ]
