from django import forms

from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',)

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
    