# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LYK_NEWS', '0004_auto_20180721_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='tittle',
            field=models.CharField(editable='False', max_length=3),
        ),
    ]
