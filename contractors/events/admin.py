from django.contrib import admin
from .models import Event, EventAdmin

# To alter readonly fields
admin.site.register(Event, EventAdmin)
