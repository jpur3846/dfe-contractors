from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime

from users.models import Contractor
from clients.models import Client
from bookers.models import Booker

class EventAdmin(admin.ModelAdmin):
    """
    Slap all of the read-only fields here to make them viewable but not editable.
    """
    readonly_fields = ('fee_incl_gst',)


class Event(models.Model):
    # Client
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    # Booker
    booker = models.ForeignKey(Booker, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    # Event Details
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=30, default='New Event')
    venue = models.CharField(max_length=30, blank=True, null=True)
    call_time = models.CharField(max_length=30, blank=True, null=True)
    fee = models.IntegerField(default=0, null=True, blank=True)
    tax = models.IntegerField(default=0, null=True, blank=True)
    # Booker signs off event is done and contractors can send invoice.
    event_complete = models.BooleanField(default=False, blank=True, null=True)

    # Musician Details
    bandleader = models.ForeignKey(Contractor, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)
    bandleader_base_fee = models.IntegerField(null=True, blank=True)
    fee_incl_gst = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        """
        # Event Details
        self.tax = self.fee//10
        
        """         # Musician Details
        if hasattr(self, 'bandleader'):
            if self.bandleader.gst_status == 'yes':
                self.fee_incl_gst = self.bandleader_base_fee*1.1 """

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} event on {self.date}."
