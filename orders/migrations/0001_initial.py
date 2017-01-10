# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('robot', '0003_auto_20170108_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.Robot', verbose_name='робот-пылесос')),
            ],
        ),
    ]