from __future__ import unicode_literals

from django.db import models
from django_unixdatetimefield import UnixDateTimeField
# Create your models here.

class Media(models.Model):
	description = models.TextField()
	format = models.CharField(blank=False, max_length=3)
	timestamp = UnixDateTimeField()
	filename = models.CharField(max_length=255)
	filesize = models.BigIntegerField()

	class Meta:
		ordering = ('created',)