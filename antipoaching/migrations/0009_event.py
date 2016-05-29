# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django_unixdatetimefield.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('antipoaching', '0008_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', max_length=500)),
                ('severity', models.CharField(choices=[('c', 'critical'), ('w', 'warning'), ('i', 'info')], default='i', max_length=1, verbose_name='severity')),
                ('timestamp', django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True)),
                ('lat', models.FloatField(default=0)),
                ('long', models.FloatField(default=0)),
                ('extra', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
