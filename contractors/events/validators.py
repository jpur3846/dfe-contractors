from django.core.exceptions import ValidationError
from django.contrib import messages

from datetime import datetime

def date_validator(date):
    """
    Validate that an event is later than today.
    """
    if date < date.today():
        raise ValidationError("Date must be later than today!")
    
    return True

def fee_positive_validator(fee):
    if fee < 0:
        raise ValidationError("Amounts must be greater than 0!")
    
    return True

def card_validator(card_type, payment_method):
    if payment_method == 'credit_card':
        if card_type == None or card_type == '':
            raise ValidationError({'card_type': 'Please select a card type!'})

    return True