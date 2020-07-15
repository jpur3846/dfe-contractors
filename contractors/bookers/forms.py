from django import forms

from .models import Booker

class BookerEditDetailsForm(forms.ModelForm):
    class Meta:
        model = Booker
        exclude = ('user', )


