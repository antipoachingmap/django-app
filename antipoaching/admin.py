from django.contrib import admin
from .models import Event
from .models import Media


admin.site.register(Event,Media)
