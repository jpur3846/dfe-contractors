from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from .validators import abn_validator, same_instrument

# Null -> DB storage
# Blank -> Form validation

yes_no_choices = [
    ('yes', 'Yes'),
    ('no', 'No')
]

# Year choices for alumni
now = datetime.now().year
year_dropdown = [(year,year) for year in range(1950, now + 6)]

cities = [
    ('sydney', 'Sydney'),
    ('melbourne', 'Melbourne'),
    ('adelaide', 'Adelaide'),
    ('brisbane', 'Brisbane'),
    ('canberra', 'Canberra'),
    ('gold_coast', 'Gold Coast')
]
states = [
    ('nsw', 'NSW'),
    ('vic', 'VIC'),
    ('act', 'ACT'),
    ('qld', 'QLD'),
    ('nt', 'NT'),
    ('wa', 'WA'),
    ('sa', 'SA'),
]
meal_preferences = [
    ('standard', 'Standard'),
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('pescetarian', 'Pescetarian'),
    ('gluten_free', 'Gluten Free'),
    ('halal', 'Halal'),
    ('kosher', 'Kosher'),
    ('dairy_free', 'Dairy Free'),
]
instruments = [
    # Chordal
    ('electric_bass', 'Electric Bass'),
    ('double_bass', 'Double Bass'),
    ('guitar', 'Guitar'),
    ('keys', 'Keys'),
    ('banjo', 'Banjo'),

    # Percussive
    ('drums', 'Drums'),
    ('percussion', 'Percussion'),

    # Vocal
    ('male_lead_vocals', 'Male Lead Vocals (For a whole gig)'),
    ('female_lead_vocals', 'Female Lead Vocals (For a whole gig)'),
    ('backing_vocals', 'Backing Vocals'),

    # Horns
    ('trumpet', 'Trumpet'),
    ('tenor_saxophone', 'Tenor Saxophone'),
    ('alto_saxophone', 'Alto Saxophone'),
    ('bari_saxophone', 'Baritone Saxophone'),
    ('soprano_saxophone', 'Soprano Saxophone'),
    ('trombone', 'Trombone'),
    ('sousaphone', 'Sousaphone'),
    
    # Classical
    ('violin', 'Violin'),
    ('viola', 'Viola'),
    ('cello', 'Cello'),
    ('oboe', 'Oboe'),
    ('cor_anglais', 'Cor Anglais'),
    ('harp', 'Harp'),

    # Electronic
    ('sound_person', 'Sound Person'),
    ('dj', 'DJ')
]

class Contractor(models.Model):
    # Personal Details
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None) # .CASCADE will delete the user account related to this contractor and vice versa.
    profile_picture = models.ImageField(null=True, blank=True, default='generic-user.jpg')
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    city = models.CharField(max_length=30, default='Sydney', null=True, choices=cities)
    state = models.CharField(max_length=3, default='NSW', null=True, choices=states)
    
    # Financial Details
    abn = models.IntegerField(validators=[abn_validator], null=True, blank=True) # 11 digits
    gst_status = models.CharField(max_length=3, default='no', blank=True, choices=yes_no_choices)
    account_name = models.CharField(max_length=50, blank=True, default='')
    bsb = models.IntegerField(blank=True, null=True)
    account_number = models.IntegerField(blank=True, null=True)

    # Musical Details
    main_instrument = models.CharField(max_length=100, null=True, blank=True, choices=instruments)
    secondary_instrument = models.CharField(max_length=100, null=True, blank=True, choices=instruments)
    other_instruments = models.CharField(max_length=400, null=True, blank=True) # CSV's
    
    # Booking details
    meal_preference = models.CharField(max_length=50, default='standard', null=True, blank=True, choices=meal_preferences)
    pa_system = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices)
    battery_amp = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices)
    public_liability = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices)
    can_mc = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) 
    number_plate = models.CharField(max_length=8, null=True, blank=True)
    accept_on_spot_requests = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices)

    # Conservatorium Stuff
    alumni = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) # yes/no. Conservatorium alumni
    year_finished = models.IntegerField(null=True, blank=True, choices=year_dropdown) # year number year

    # Denylisted - are they banned?
    denylisted = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        """
        Overwrites save and will allow some fields to auto update on save.
        """
        if self.number_plate != None:
            self.number_plate = self.number_plate.upper()
        

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name: {self.user.first_name} {self.user.last_name} | Email: {self.user.email} | Ex-Student: {self.alumni}'

    def clean(self):
        """
        Extends clean. Will raise error if any of the fields do not pass.
        """
        same_instrument(self.main_instrument, self.secondary_instrument) # main and secondary are diff insts.