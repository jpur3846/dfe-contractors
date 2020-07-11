from django.db import models
from django.contrib.auth.models import User
from users.models import Contractor

class Event(models.Model):
    date = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    call_time = models.CharField(max_length=30)
    fee_incl_gst = models.IntegerField()
    bandleader = models.ForeignKey(Contractor, on_delete=models.PROTECT, related_name='events', default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name} event on {self.date}."