# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170729_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['collection', 'section', 'pos'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
