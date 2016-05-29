from django.contrib import admin

# Register your models here.


from .models import Event
# admin.site.register(Event )

class EventAdmin(admin.ModelAdmin):
    list_display = ('severity', 'description', 'timestamp')
admin.site.register(Event, EventAdmin)

from .models import Media
admin.site.register(Media )
