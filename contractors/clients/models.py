from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    general_info = models.TextField(default='')

    def __str__(self):
        return f'Client: {self.user.first_name} {self.user.last_name} | Email: {self.user.username}'
