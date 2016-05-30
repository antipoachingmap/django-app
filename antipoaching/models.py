from mongoengine import *


class Extra(EmbeddedDocument):
	animals = DictField()
	details = StringField()

class Event(Document):
    description = StringField()
    severity = StringField()
    timestamp = IntField()
    lat = FloatField(default=0)
    lng = FloatField(default=0)
    extra = EmbeddedDocumentField(Extra)

class Media(Document):
	description = StringField()
	format = StringField()
	timestamp = IntField()
	filename = StringField()
	filesize = IntField()
	event = ReferenceField('Event')
