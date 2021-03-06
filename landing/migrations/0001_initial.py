# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-16 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import landing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField(default=0, help_text='От меньшего к большему', verbose_name='позиция')),
                ('show', models.BooleanField(default=True, verbose_name='показывать')),
                ('title', models.CharField(max_length=140, verbose_name='название')),
                ('url', models.CharField(default='ivanov', max_length=20, verbose_name='url')),
                ('created', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('modefied', models.DateField(auto_now=True, verbose_name='дата изменения')),
                ('img', models.ImageField(upload_to=landing.models.collection_path, verbose_name='обложка')),
            ],
            options={
                'verbose_name': 'коллекция',
                'verbose_name_plural': 'коллекции',
                'ordering': ['pos'],
            },
        ),
    ]
