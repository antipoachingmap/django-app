# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0002_auto_20160529_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('format', models.CharField(max_length=3)),
                ('timestamp', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('filename', models.CharField(max_length=255)),
                ('filesize', models.BigIntegerField()),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
