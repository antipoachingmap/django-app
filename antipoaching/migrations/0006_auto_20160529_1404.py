# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0005_auto_20160529_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='longitude',
            new_name='long',
        ),
    ]