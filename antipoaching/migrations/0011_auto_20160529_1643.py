# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0010_auto_20160529_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='media',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]
