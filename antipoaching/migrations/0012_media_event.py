# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0011_auto_20160529_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='antipoaching.Event'),
        ),
    ]
