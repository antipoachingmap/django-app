from __future__ import unicode_literals

from django.db import models
from django_unixdatetimefield import UnixDateTimeField
# import jsonfield
from jsonfield import JSONField



SEVERITY_CHOICES = [('c', "critical"), ('w', "warning"), ('i', "info")]


class Event(models.Model):
    description = models.TextField(max_length=500, default='')
    severity = models.CharField(('severity'), choices=SEVERITY_CHOICES, default='i', max_length=1)
    timestamp = UnixDateTimeField(auto_now_add=True)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    # media
    # extra = jsonfield.JSONField()
    extra = JSONField(null=True, default="")


class Media(models.Model):
	description = models.TextField()
	format = models.CharField(blank=False, max_length=3)
	timestamp = UnixDateTimeField()
	filename = models.CharField(max_length=255)
	filesize = models.BigIntegerField()
	class Meta:
		ordering = ('timestamp',)
