# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-22 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LYK_NEWS', '0012_auto_20180722_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='content',
            field=models.TextField(default='{dir(models)}'),
        ),
    ]