# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['pos'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
    ]
