# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'verbose_name': 'робот-пылесос', 'verbose_name_plural': 'роботы-пылесосы'},
        ),
    ]
