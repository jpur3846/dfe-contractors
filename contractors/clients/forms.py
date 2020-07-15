from django import forms

from .models import Client

class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('contact_name',)