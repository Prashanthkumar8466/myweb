# Generated by Django 3.2.25 on 2024-08-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_rename_whatsapp_link_footer_whatsapp_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pop_Name', models.CharField(max_length=50)),
                ('popup_message', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
