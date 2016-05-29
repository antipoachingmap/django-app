from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField

SEVERITY_CHOICES = [('c', "critical"), ('w', "warning"), ('i', "info")]

class Event(models.Model):
    description = models.TextField(max_length=500, default='')
    severity = models.CharField(('severity'), choices=SEVERITY_CHOICES, default='i', max_length=1)
    timestamp = models.IntegerField()
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    extra = JSONField(null=True, default="")

class Media(models.Model):
	description = models.TextField()
	format = models.CharField(blank=False, max_length=3)
	timestamp = models.IntegerField()
	filename = models.CharField(max_length=255)
	filesize = models.BigIntegerField()
	class Meta:
		ordering = ('timestamp',)
