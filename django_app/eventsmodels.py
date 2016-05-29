from __future__ import unicode_literals

from django.db import models


SEVERITY_CHOICES = [('c', "critical"), ('w', "warning"), ('i', "info")]


class Event(models.Model):
	description = models.TextField(max_length=500)
	severity = models.CharField(('severity'), choices=SEVERITY_CHOICES, default='i')

	def __str__(self):
		return self.title + " " + str(self.year)