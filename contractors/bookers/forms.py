from django import forms

from .models import Booker

class BookerEditDetailsForm(forms.ModelForm):
    profile_picture = forms.ImageField()

    class Meta:
        model = Booker
        exclude = ('user', )