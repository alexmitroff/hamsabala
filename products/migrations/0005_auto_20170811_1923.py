# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-11 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170730_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.product_path, verbose_name='cover'),
        ),
    ]