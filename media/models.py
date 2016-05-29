from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.

class Media(Document):
  description = StringField(max_length=200)
  format = StringField(max_length=3)
  timestamp = UnixDateTimeField()
  filesize = IntField()
  data = BinaryField()