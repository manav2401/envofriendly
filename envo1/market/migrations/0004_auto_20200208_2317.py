# Generated by Django 3.0.3 on 2020-02-08 23:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_product_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='productsBought',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
