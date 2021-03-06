# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170729_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='section',
            name='cover',
            field=models.ImageField(blank=True, help_text='wide 16:9', null=True, upload_to=products.models.section_path, verbose_name='cover'),
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='section',
            name='img',
            field=models.ImageField(blank=True, help_text='square 1:1', null=True, upload_to=products.models.section_path, verbose_name='img'),
        ),
    ]
