# Generated by Django 3.2.8 on 2021-10-19 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('license_key_shop', '0006_key_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextended',
            name='owner',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_extended', to=settings.AUTH_USER_MODEL),
        ),
    ]
