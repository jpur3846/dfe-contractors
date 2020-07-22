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
        exclude = ('musicians', 'booker',)
        
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Event Name'}),
            'date': DateInput(attrs= {'class': 'form-control', 'placeholder': 'Event Date'}),
            'event_complete': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'event_completion_status': forms.Select(attrs= {'class': 'form-control'}),
            'event_status': forms.Select(attrs= {'class': 'form-control'}),
            'band_locked_in': forms.CheckboxInput(attrs= {'class': 'form-control'}),

            'contract_sent': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'contract_signed': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'invoice_sent': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'deposit_paid': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'balance_paid': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'calendar_event_created': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'client_followup': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'band_locked_in': forms.CheckboxInput(attrs= {'class': 'form-control'}),

            'booker': forms.Select(attrs= {'class': 'form-control'}),
            'gig_source': forms.Select(attrs= {'class': 'form-control'}),

            'client': forms.Select(attrs= {'class': 'form-control'}),

            'band_lineup': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Band Lineup'}),
            'rehearsal': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Rehearsal Details'}),

            'venue': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Venue'}),
            'venue_in_case_of_rain': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Venue in case of rain'}),

            'parking_provided': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'number_parking_spots_required': forms.NumberInput(attrs= {'class': 'form-control'}),
            'parking_cost_per_car': forms.NumberInput(attrs= {'class': 'form-control'}),
            'parking_address': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Parking address'}),
            'parking_assignment': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Parking Assignment'}),
            'loading_zone_details': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Loading zone details'}),

            'booking_start_time': TimeInput(attrs= {'class': 'form-control', 'placeholder': 'Booking Start Time'}),
            'booking_end_time': TimeInput(attrs= {'class': 'form-control', 'placeholder': 'Booking End Time'}),
            'musicians_call_time': TimeInput(attrs= {'class': 'form-control', 'placeholder': 'Musicians Call Time'}),

            'musicians_attire': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Attire'}),
            'musical_style': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Musical Style'}),
            'production': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Production/AV'}),

            'power_required': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'crew_meals': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'run_sheet': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Runsheet details'}),

            'important_requests': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Important requests'}),
            'general_requests': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'General requests'}),
            'do_not_play': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Do not play'}),
            'further_musician_requirements': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Further musician requirements'}),
            'musician_only_notes': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Musician ONLY notes'}),

            'helpful_files': forms.FileInput(),

            # Leaving out certain financial fields as they will be calculated.
            'total_fee_no_gst': forms.NumberInput(attrs= {'class': 'form-control'}),
            'deposit_required': forms.CheckboxInput(attrs= {'class': 'form-control'}),
            'payment_method': forms.Select(attrs= {'class': 'form-control'}),
            'card_type': forms.Select(attrs= {'class': 'form-control'}),
            'deposit_and_surcharge': forms.NumberInput(attrs= {'class': 'form-control'}),
            'balance_and_surcharge': forms.NumberInput(attrs= {'class': 'form-control'}),
            'booker_fee': forms.NumberInput(attrs= {'class': 'form-control'}),

            'booker_payment_status': forms.Select(attrs= {'class': 'form-control'}),
            'business_payment_status': forms.Select(attrs= {'class': 'form-control'}),

            'asked_musicians': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Asked musicians'}),
            'unavailable_musicians': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'Unavailable musicians'}),
        }

class AddEventMusician(forms.ModelForm):
    class Meta:
        model = EventMusicians
        fields = ('contractor', )

        widgets = {
            'contractor': forms.Select(attrs= {'class': 'form-control'}),
        }

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
    