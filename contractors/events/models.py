from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime

# from users.models import Contractor
from clients.models import Client
from bookers.models import Booker
from users.models import Contractor

class EventAdmin(admin.ModelAdmin):
    """
    Slap all of the read-only fields here to make them viewable but not editable. Only works in the Django admin. 
    For the booker forms this is is taken care of by listing fields individually
    """
    readonly_fields = ('total_fee_incl_gst',)

yes_or_no = [
    ('yes', 'Yes'),
    ('no', 'No')
]
event_statuses = [
    ('locked_in', 'Locked in'),
    ('locked_in_via_email', 'Locked In Via Email'),
    ('tentative', 'Tentative')
]
event_completion_statuses = [
    ('awaiting_balance', 'Awaiting Balance'),
    ('awaiting_balance_and_deposit', 'Awaiting Balance and Deposit'),
    ('awaiting_musician_invoices', 'Awaiting Musician Invoices'),
    ('awaiting_balance', 'Cancelled'),
    ('postponed', 'Postponed'),
    ('complete', 'Complete')
]
gig_sources = [
    ('word_of_mouth', 'Word Of Mouth'),
    ('general', 'General'),
    ('usyd', 'USYD'),
    ('website', 'Website'),
    ('busking', 'Busking'),
]
payment_methods = [
    ('direct_deposit', 'Direct Deposit'),
    ('poli', 'POLI'),
    ('credit_card', 'Credit Card'),
    ('cash', 'Cash'),
]
card_types = [
    ('domestic', 'Domestic'),
    ('international', 'International'),
]

class Event(models.Model):
    ### Event Basic Details
    name = models.CharField(max_length=60, default='New Event')
    date = models.DateField(blank=True, null=True)
    event_complete = models.BooleanField(default=False, blank=True, null=True)
    event_completion_status = models.CharField(max_length=50, default='Awaiting Balance and Deposit', blank=True, null=True, choices=event_completion_statuses)
    event_status = models.CharField(max_length=20, default='Tentative', blank=True, null=True, choices=event_statuses)
    band_locked_in = models.BooleanField(default=False, blank=True, null=True)
    # Contract number is PK + 500 (starting from 500th invoice.)

    ### To Do List
    contract_sent = models.BooleanField(default=False, blank=True, null=True)
    contract_signed = models.BooleanField(default=False, blank=True, null=True)
    invoice_sent = models.BooleanField(default=False, blank=True, null=True)
    deposit_paid = models.BooleanField(default=False, blank=True, null=True)
    balance_paid = models.BooleanField(default=False, blank=True, null=True)
    calendar_event_created = models.BooleanField(default=False, blank=True, null=True)
    client_followup = models.BooleanField(default=False, blank=True, null=True)
    # Musician to do
    band_locked_in = models.BooleanField(default=False, blank=True, null=True)

    ### Booker
    booker = models.ForeignKey(Booker, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)
    gig_source = models.CharField(max_length=20, default='Word Of Mouth', blank=True, null=True, choices=gig_sources)

    ### Client
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    ### Further Details
    band_lineup = models.CharField(max_length=100, blank=True, null=True)
    rehearsal = models.CharField(max_length=100, default='Not Required', blank=True, null=True)

    # Locations
    venue = models.CharField(max_length=100, blank=True, null=True)
    venue_in_case_of_rain = models.CharField(max_length=100, blank=True, null=True)
    parking_provided = models.CharField(max_length=50, default='Not Required', blank=True, null=True)
    number_parking_spots_required  = models.IntegerField(blank=True, null=True)
    parking_cost_per_car = models.FloatField(blank=True, null=True)
    parking_address = models.CharField(max_length=100, blank=True, null=True)
    loading_zone_details = models.CharField(max_length=100, blank=True, null=True)
    # Timings
    booking_start_time = models.TimeField(blank=True, null=True)
    booking_end_time = models.TimeField(blank=True, null=True)
    musicians_call_time = models.TimeField(blank=True, null=True)
    # General Music Details
    musicians_attire = models.CharField(max_length=100, default='Smart Casual', blank=True, null=True)
    musical_style = models.CharField(max_length=100, blank=True, null=True)
    production = models.CharField(max_length=100, blank=True, null=True)
    power_required = models.BooleanField(default=True)
    crew_meals = models.BooleanField(default=False)
    run_sheet = models.TextField(blank=True, null=False)
    # Additional Information
    important_requests = models.TextField(blank=True, null=False)
    general_requests = models.TextField(blank=True, null=False)
    do_not_play = models.TextField(blank=True, null=False)
    further_musician_requirements = models.TextField(blank=True, null=False)
    musician_only_notes = models.TextField(blank=True, null=False)
    parking_assignment = models.TextField(blank=True, null=False) # Select from musicians?

    ### File Upload (runsheet)
    helpful_files = models.FileField(upload_to='event_uploads/%Y/%m/%d/', null=True, blank=True)

    ### Financial Details
    total_fee_no_gst = models.FloatField(blank=True, null=True)
    deposit_required = models.BooleanField(default=True, blank=True, null=True)
    payment_method = models.CharField(max_length=30, blank=True, null=True, choices=payment_methods)
    card_type = models.CharField(max_length=30, blank=True, null=True, choices=card_types)
    total_fee_incl_gst = models.FloatField(default=0, blank=True, null=True)
    credit_card_surcharge_amount = models.FloatField(default=0, blank=True, null=True)
    total_fee_incl_all = models.FloatField(default=0, blank=True, null=True)
    deposit_and_surcharge = models.FloatField(default=0, blank=True, null=True)
    balance_and_surcharge = models.FloatField(default=0, blank=True, null=True)
    booker_fee = models.FloatField(default=0, blank=True, null=True)
    total_gst_amount = models.FloatField(default=0, blank=True, null=True)
    # Payments
    booker_payment_status = models.BooleanField(default=False, blank=True, null=True)
    business_payment_status = models.BooleanField(default=False, blank=True, null=True)

    ### Musician Details
    asked_musicians = models.TextField(null=True, blank=True)
    unavailable_musicians = models.TextField(null=True, blank=True)

    musicians = models.ManyToManyField(Contractor, through='EventMusicians')
    # bandleader = models.ForeignKey(Contractor, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        """
        """
        Event Details
        self.tax = self.fee//10
        
        # Musician Details
        if hasattr(self, 'musician_2'):
            if self.musician_2.gst_status == 'yes':
                self.fee_incl_gst = self.musician_2_base_fee*1.1 """

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} event on {self.date}."

class EventMusicians(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    is_bandleader = models.BooleanField(default=False, blank=True, null=True)
    fee = models.IntegerField(null=True, blank=True) # Incl. Parking, Leader fee etc. Excl. GST
    gst_amnt = models.FloatField(null=True, blank=True)
    fee_all_incl = models.FloatField(null=True, blank=True)
    feedback_status = models.BooleanField(default=False, blank=True, null=True)
    invoice_status = models.BooleanField(default=False, blank=True, null=True)
    payment_status = models.BooleanField(default=False, blank=True, null=True)