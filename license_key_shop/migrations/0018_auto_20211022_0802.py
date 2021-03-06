# Generated by Django 3.2.8 on 2021-10-22 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('license_key_shop', '0017_rename_owner_userextended_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextended',
            name='alert_key_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='key_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_extended', to=settings.AUTH_USER_MODEL),
        ),
    ]
