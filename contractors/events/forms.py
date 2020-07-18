from django import forms

from .models import Event, EventMusicians

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',)

class EventEditForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('musicians',)

class AddEventMusician(forms.ModelForm):
    class Meta:
        model = EventMusicians
        fields = ('contractor', )

class EditEventMusician(forms.ModelForm):
    class Meta:
        model = EventMusicians
        exclude = (
            'event',
        )
    