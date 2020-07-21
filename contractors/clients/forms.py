from django import forms

from .models import Client

class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs= {'class': 'form-control'}),
            'company': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Company'}),
            'contact_name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Name'}),
            'contact_email': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Contact Email'}),
            'contact_number': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Contact Number'}),
            'general_info': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'General Information'}),
        }

class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('contact_name',)

        widgets = {
            'contact_name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Client Name'}),
        }