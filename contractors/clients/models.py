from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    """
    Some of the client data will be duplicated from the user as
    bookers will need to be able to create and edit client details.
    A client may be granted a user account if they would like to see the event details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    company = models.CharField(max_length=30, default='', blank=True)
    contact_name = models.CharField(max_length=30, default='')
    contact_email = models.EmailField(max_length=30, default='', blank=True)
    contact_number = models.IntegerField(null=True, blank=True)

    general_info = models.TextField(default='', blank=True)

    def __str__(self):
        return f'Client: {self.contact_name} | Company: {self.company} | Email: {self.contact_email}'
