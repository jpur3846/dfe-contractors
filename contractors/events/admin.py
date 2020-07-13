from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    """
    Slap all of the read-only fields here.
    """
    readonly_fields = ('fee_incl_gst',)

admin.site.register(Event, EventAdmin)