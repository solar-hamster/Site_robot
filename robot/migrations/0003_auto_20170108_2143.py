# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0002_auto_20170105_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'ordering': ['name'], 'verbose_name': 'робот-пылесос', 'verbose_name_plural': 'роботы-пылесосы'},
        ),
        migrations.AddField(
            model_name='robot',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='robot/photes', verbose_name='фотография'),
        ),
    ]