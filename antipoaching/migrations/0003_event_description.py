# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0002_auto_20160529_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
