from django.contrib import admin
from .models import Event, EventAdmin, EventMusicians

# To alter readonly fields
admin.site.register(Event, EventAdmin)
admin.site.register(EventMusicians)
