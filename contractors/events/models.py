from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError

from datetime import datetime
from decimal import *

# from users.models import Contractor
from clients.models import Client
from bookers.models import Booker
from users.models import Contractor
from events.validators import (
    date_validator,
    fee_positive_validator,
    card_validator
    )

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
    date = models.DateField(null=True)
    event_complete = models.BooleanField(blank=True, null=True, default=False)
    event_completion_status = models.CharField(max_length=50, default='awaiting_balance_and_deposit', blank=True, null=True, choices=event_completion_statuses)
    event_status = models.CharField(max_length=20, default='tentative', blank=True, null=True, choices=event_statuses)
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
    email_worksheet_reminder = models.BooleanField(default=False, blank=True)
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
    parking_provided = models.BooleanField(max_length=50, default=False, blank=True, null=True)
    number_parking_spots_required = models.IntegerField(blank=True, null=True, default=0)
    parking_cost_per_car = models.FloatField(blank=True, null=True, default=0)
    parking_address = models.CharField(max_length=100, default='Near Venue', blank=True, null=True)
    parking_assignment = models.TextField(blank=True, null=False) # Select from musicians?
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
    run_sheet = models.TextField(blank=True, null=True)
    # Additional Information
    important_requests = models.TextField(blank=True, null=False)
    general_requests = models.TextField(blank=True, null=False)
    do_not_play = models.TextField(blank=True, null=False)
    further_musician_requirements = models.TextField(blank=True, null=False)
    musician_only_notes = models.TextField(blank=True, null=False)

    ### File Upload (runsheet)
    helpful_files = models.FileField(upload_to='event_uploads/%Y/%m/%d/', null=True, blank=True)

    ### Financial Details
    total_fee_no_gst = models.FloatField(default=0, blank=True, null=True) # Total fee that can be taxed (so not including fees etc.) 
    deposit_required = models.BooleanField(default=True, blank=True, null=True)
    payment_method = models.CharField(max_length=30, blank=True, null=True, choices=payment_methods, default='direct_deposit')
    card_type = models.CharField(max_length=30, blank=True, choices=card_types, default='domestic')
    booker_fee = models.FloatField(default=0, blank=True, null=True)

    gst_amount = models.FloatField(default=0, blank=True, null=True) # GST
    parking_total = models.FloatField(default=0, blank=True, null=True)
    total_fee_incl_gst = models.FloatField(default=0, blank=True, null=True) # Fee + GST + inclusions
    
    credit_card_surcharge_amount = models.FloatField(default=0, blank=True, null=True)
    deposit_and_surcharge = models.FloatField(default=0, blank=True, null=True)
    balance_and_surcharge = models.FloatField(default=0, blank=True, null=True)
    
    total_fee_incl_all = models.FloatField(default=0, blank=True, null=True) # The fee we send to the client w/ surcharges etc
    # Payments
    booker_payment_status = models.BooleanField(default=False, blank=True, null=True)
    business_payment_status = models.BooleanField(default=False, blank=True, null=True)

    ### Musician Details
    asked_musicians = models.TextField(null=True, blank=True)
    unavailable_musicians = models.TextField(default=',', null=True, blank=True)

    musicians = models.ManyToManyField(Contractor, through='EventMusicians')

    def is_complete(self):
        event_complete = self.contract_sent and self.contract_signed and self.invoice_sent  and self.deposit_paid \
                    and self.balance_paid and self.client_followup and self.band_locked_in and self.event_complete \
                        and (self.event_completion_status == 'complete')

        return event_complete

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        Do the calculations first then format.
        NB: No GST charged on billable expenses eg parking
        """
        TWOPLACES = Decimal(10) ** -2
        ### Calculations ###
        self.gst_amount = self.calculate_gst()
        self.total_fee_incl_gst = self.gst_amount + self.total_fee_no_gst # Total fee before parking
        self.parking_total = self.calculate_parking() # Parking
        base_costs = self.parking_total + self.total_fee_incl_gst # Sum of parking and total.

        deposit = self.calculate_deposit(base_costs)
        balance = self.calculate_balance(base_costs)
        deposit_surcharge = self.calculate_surcharge(deposit)
        balance_surcharge = self.calculate_surcharge(balance)
        self.credit_card_surcharge_amount = deposit_surcharge + balance_surcharge

        self.deposit_and_surcharge = deposit + deposit_surcharge
        self.balance_and_surcharge = balance + balance_surcharge

        self.total_fee_incl_all = self.deposit_and_surcharge + self.balance_and_surcharge

        ### Format outputs. ###

        super().save(*args, **kwargs)

    def calculate_gst(self):
        if self.payment_method == 'cash':
            return 0
        return float(self.total_fee_no_gst*0.1)

    def calculate_parking(self):
        return self.number_parking_spots_required * self.parking_cost_per_car

    def calculate_deposit(self, value):
        """
        Calculate 25% deposit before payment surcharges added.
        """
        if self.deposit_required:
            deposit = (value/4)
        else:
            return 0

        return deposit

    def calculate_balance(self, value):
        """
        Calculate balance before payment surcharge added
        """
        balance = value

        if self.deposit_required:
            balance = value - self.calculate_deposit(value)

        return balance

    def calculate_surcharge(self, value):
        """ Calculate a POLi or Stripe surcharge on a payment """
        surcharge = 0
        if value == 0:
            return 0 # Means we are not going to add 30c for a null transaction
        elif self.payment_method == 'poli':
            surcharge += Event.poli_fee(value)
        elif self.payment_method == 'credit_card':
            surcharge += self.card_fee(value)
        
        return surcharge

    def card_fee(self, value):
        """ Returns fee for paying via credit card on stripe """
        card_rate = self.credit_card_rate()/100
        fee = (value + 0.3)/(1-card_rate) - value
        return fee

    def credit_card_rate(self):
        """
        Returns the rate of a card.
        """
        if self.payment_method != 'credit_card':
            return 0
            
        if self.card_type == 'domestic':
            return 1.75
        elif self.card_type == 'international':
            return 2.90

    def poli_fee(value):
        """ POLi charges 1% per transaction up to $3. Returns the fee """
        fee = value*0.01
        if fee > 3:
            return 3
        return fee
    
    def calculate_musicians_base_fees(self):
        """ Calculate the costs for all musicians incl everything """
        musicians = self.eventmusicians_set.all()
        total_musicians_fees = 0

        for musician in musicians:
            total_musicians_fees += musician.fee

        return total_musicians_fees

    def calculate_musicians_gst(self):
        musicians = self.eventmusicians_set.all()
        total_musicians_gst = 0

        for musician in musicians:
            total_musicians_gst += musician.gst_amnt

        return total_musicians_gst

    def calculate_musicians_inclusions(self):
        musicians = self.eventmusicians_set.all()
        total_musicians_inclusions = 0

        for musician in musicians:
            total_musicians_inclusions += musician.inclusions

        return total_musicians_inclusions

    def calculate_gst_payable(self):
        return self.calculate_gst() - self.calculate_musicians_gst()

    def calculate_business_profits(self):
        profit = self.total_fee_incl_all - \
            self.calculate_musicians_base_fees() - \
            self.calculate_musicians_inclusions() - \
            self.credit_card_surcharge_amount - \
            self.booker_fee - \
            self.calculate_parking() - \
            self.credit_card_surcharge_amount - \
            self.gst_amount

        return profit

    def get_musicians_emails(self):
        emails = []
        for musician in self.eventmusicians_set.all():
            emails.append(musician.contractor.user.email)

        return emails

    def __str__(self):
        return f"{self.name} event on {self.date}."

    def clean(self):
        """ Extend clean method """
        card_validator(self.card_type, self.payment_method)
        if self.payment_method != 'credit_card':
            self.card_type == None

class EventMusicians(models.Model):
    is_available = models.BooleanField(default=None, null=True, blank=True)
    email_invite_sent = models.BooleanField(default=False, blank=True)
    
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    is_bandleader = models.CharField(max_length=4, default='no', choices=yes_or_no, blank=True, null=True)
    instrument = models.CharField(max_length=100, default='', blank=True, null=True)
    
    fee = models.IntegerField(null=True, blank=True, default=0, validators=[fee_positive_validator]) # Base Fee
    inclusions = models.FloatField(null=True, default=0, validators=[fee_positive_validator])
    gst_amnt = models.FloatField(null=True, blank=True, default=0, validators=[fee_positive_validator])
    fee_all_incl = models.FloatField(null=True, blank=True, default=0, validators=[fee_positive_validator])
    
    feedback_status = models.CharField(max_length=3, choices=yes_or_no, default='no', blank=True, null=True)
    invoice_status = models.CharField(max_length=3, choices=yes_or_no, default='no', blank=True, null=True)
    payment_status = models.CharField(max_length=3, choices=yes_or_no, default='no', blank=True, null=True)

    def __str__(self):
        return f'{self.contractor.user.first_name} {self.contractor.user.last_name} | \n \
            {self.contractor.user.email} | {self.contractor.phone_number}'

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        """

        gst, fee_all_incl = self.calculate_fee_all_incl()

        self.gst_amnt = gst
        self.fee_all_incl = fee_all_incl

        super().save(*args, **kwargs)

    def calculate_fee_all_incl(self):
        base_fee = self.fee
        inclusions = self.inclusions
        gst = 0
        
        fee_all_incl = base_fee + inclusions

        if self.contractor.gst_status == 'yes':
            gst = float(base_fee*0.1)

        fee_all_incl += gst

        return (gst, fee_all_incl)

        