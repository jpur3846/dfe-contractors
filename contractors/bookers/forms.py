from django import forms

from .models import Booker

class BookerEditDetailsForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Booker
        fields = (
            'contact_number',
            'profile_picture',
        )
        exclude = ('user', 'contact_email')

        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'contact_number': forms.NumberInput(attrs= {'class': 'form-control'})
        }