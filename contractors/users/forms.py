from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contractor

class ContractorProfileForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ('instrument',)
    
    # Field is not required.
    def __init__(self, *args, **kwargs):
        super(ContractorProfileForm, self).__init__(*args, **kwargs)
        self.fields['instrument'].required = False