from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime

from users.models import Contractor
from clients.models import Client

class EventAdmin(admin.ModelAdmin):
    """
    Slap all of the read-only fields here.
    The event admin is the booking manager that can create events etc etc.
    """
    readonly_fields = ('fee_incl_gst',)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)


class Event(models.Model):
    # Client
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    # Event Details
    date = models.DateField()
    name = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    call_time = models.CharField(max_length=30)
    fee = models.IntegerField(null=True)
    tax = models.IntegerField(null=True)
    # Booker signs off event is done and contractors can send invoice.
    event_complete = models.BooleanField(default=False)

    # Musician Details
    bandleader = models.ForeignKey(Contractor, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)
    bandleader_base_fee = models.IntegerField(null=True)
    fee_incl_gst = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        """
        # Event Details
        self.tax = self.fee//10
        
        # Musician Details
        if self.bandleader.gst_status == 'yes':
            self.fee_incl_gst = self.bandleader_base_fee*1.1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} event on {self.date}."
