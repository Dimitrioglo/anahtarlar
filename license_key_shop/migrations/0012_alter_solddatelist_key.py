# Generated by Django 3.2.8 on 2021-10-19 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license_key_shop', '0011_alter_key_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solddatelist',
            name='key',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_key', to='license_key_shop.key'),
        ),
    ]
