# Generated by Django 3.2.8 on 2021-10-20 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license_key_shop', '0015_auto_20211020_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextended',
            name='user_status',
        ),
    ]
