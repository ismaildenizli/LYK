# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LYK_NEWS', '0006_auto_20180721_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='date_creation',
            field=models.DateTimeField(error_messages={'invalid': 'ahaha'}),
        ),
    ]