# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
