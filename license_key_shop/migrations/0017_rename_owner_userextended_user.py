# Generated by Django 3.2.8 on 2021-10-21 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license_key_shop', '0016_remove_userextended_user_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userextended',
            old_name='owner',
            new_name='user',
        ),
    ]
