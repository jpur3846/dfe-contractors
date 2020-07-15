from django.db import models
from django.contrib.auth.models import User

class Booker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    contact_email = models.EmailField(null=True)
    contact_number = models.IntegerField(null=True)
    
    def __str__(self):
        return f'Booker: {self.user.first_name} {self.user.last_name} | Email: {self.user.email}'