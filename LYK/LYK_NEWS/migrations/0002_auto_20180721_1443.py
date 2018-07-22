# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LYK_NEWS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='date_publish',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='news_locale',
            field=models.CharField(choices=[('TR', 'TURKEY'), ('ENG', 'ENGLAND'), ('SWE', 'SWEDEN')], default='CHOOSE', max_length=3),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='date_creation',
            field=models.DateTimeField(),
        ),
    ]