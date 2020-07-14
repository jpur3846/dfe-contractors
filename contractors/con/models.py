from django.db import models
from django.contrib.auth.models import User

class ConStaff(models.Model):
    """
    For con staff to access specific insights.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'Con Staff'