from django import forms

from .models import Event, EventMusicians

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'date',
            'name',
            'venue',
            'booking_start_time',
            'total_fee_no_gst',
            )
        
        widgets = {
            'date': DateInput(attrs= {'class': 'form-control', 'placeholder': 'Event Date'}),
            'name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Event Name'}),
            'venue': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Venue'}),
            'booking_start_time': TimeInput(attrs= {'class': 'form-control', 'placeholder': 'Booking Start Time'}),
            'total_fee_no_gst': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Fee (No GST)'}),
        }

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
            'contractor',
        )

        widgets = {
            'is_bandleader': forms.Select(attrs= {'class': 'form-control'}),
            'instrument': forms.TextInput(attrs= {'class': 'form-control'}),
            'fee': forms.TextInput(attrs= {'class': 'form-control'}),
            'gst_amnt': forms.TextInput(attrs= {'class': 'form-control'}),
            'feedback_status': forms.Select(attrs= {'class': 'form-control'}),
            'invoice_status': forms.Select(attrs= {'class': 'form-control'}),
            'payment_status': forms.Select(attrs= {'class': 'form-control'}),
        }
    