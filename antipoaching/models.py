from __future__ import unicode_literals

from django.db import models

# Create your models here.



SEVERITY_CHOICES = [('c', "critical"), ('w', "warning"), ('i', "info")]


class Event(models.Model):
    description = models.TextField(max_length=500)
    severity = models.CharField(('severity'), choices=SEVERITY_CHOICES, default='i', max_length=1)


    # email = models.EmailField(null=True, default="",blank=True)
    # type = models.CharField(('type'), choices=USERTYPES, default='r', max_length=1)
    # def __str__(self):
    #     return self.name