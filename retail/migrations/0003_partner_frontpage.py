# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_auto_20170729_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='frontpage',
            field=models.BooleanField(default=True, help_text='Show on front page', verbose_name='frontpage'),
        ),
    ]
