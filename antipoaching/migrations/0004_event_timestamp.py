# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0003_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timestamp',
            field=django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 29, 13, 41, 51, 882425, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
