from __future__ import unicode_literals

from django.db import models
from django_unixdatetimefield import UnixDateTimeField
# Create your models here.




SEVERITY_CHOICES = [('c', "critical"), ('w', "warning"), ('i', "info")]


class Event(models.Model):
    description = models.TextField(max_length=500, default='')
    severity = models.CharField(('severity'), choices=SEVERITY_CHOICES, default='i', max_length=1)
    timestamp = UnixDateTimeField(auto_now_add=True)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    #
    # email = models.EmailField(null=True, default="",blank=True)
    # type = models.CharField(('type'), choices=USERTYPES, default='r', max_length=1)
    # def __str__(self):
    #     return self.name