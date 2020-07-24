from django.core.exceptions import ValidationError

from datetime import datetime

def date_validator(date):
    """
    Validate that an event is later than today.
    """
    if date < date.today():
        raise ValidationError("Date must be later than today!")
    
    return True