from django.core.exceptions import ValidationError

def abn_validator(abn):
    """
    Checks that x is 11 chars long.
    """
    abn = str(abn)
    
    if len(abn) != 11:
        raise ValidationError("The ABN you have entered is not valid.")

def same_instrument(inst_1, inst_2):
    """
    Checks if someone has tried to list 2 of the instruments as their primary and secondary instrument.
    """
    if (inst_1 == inst_2 != None):
        raise ValidationError({'secondary_instrument': "Instrument 1 and 2 cannot be the same instrument."})
