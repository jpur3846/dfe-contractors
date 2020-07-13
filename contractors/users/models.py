from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# Null -> DB storage
# Blank -> Form validation

yes_no_choices = [
    ('yes', 'Yes'),
    ('no', 'No')
]

# Year choices for alumni
now = datetime.now().year
year_dropdown = [(year,year) for year in range(1950, now + 6)]

class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None) # .CASCADE will delete the user account related to this contractor and vice versa.
    profile_picture = models.ImageField(null=True, blank=True, default='generic-user.jpg')   
    phone_number = models.IntegerField(null=True, blank=True)

    main_instrument = models.CharField(max_length=100, null=True, blank=True)
 
    city = models.CharField(max_length=100, default='Sydney', null=True)

    public_liability = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) # yes/no

    pa_system = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) # yes/no
    battery_amp = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) # yes/no

    alumni = models.CharField(max_length=3, null=True, blank=True, choices=yes_no_choices) # yes/no. Conservatorium alumni
    year_finished = models.IntegerField(null=True, blank=True, choices=year_dropdown) # year number year

    def __str__(self):
        return f'Name: {self.user.first_name} {self.user.last_name} | Email: {self.user.email}'