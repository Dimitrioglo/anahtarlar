# Generated by Django 3.2.8 on 2021-10-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('license_key_shop', '0010_auto_20211019_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_key', to='license_key_shop.product'),
        ),
    ]