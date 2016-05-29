from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Media(models.Model):
	description = models.TextField()
	format = models.CharField(blank=False, max_length=3)
	timestamp = models.IntegerField()
	filename = models.CharField(max_length=255)
	filesize = models.BigIntegerField()

	class Meta:
		ordering = ('timestamp',)