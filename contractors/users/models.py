from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contractor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None) # .CASCADE will delete the user account related to this contractor and vice versa.
    instrument = models.CharField(max_length=100, default=None, null=True)
    profile_picture = models.ImageField(null=True, blank=True, default='generic-user.jpg')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.username}'