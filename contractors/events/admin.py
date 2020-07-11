from django.contrib import admin

# Register your models here.

from .models import Contractor, Event

admin.site.register(Contractor)
admin.site.register(Event)