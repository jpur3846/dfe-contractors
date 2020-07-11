from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Contractor

# Widgets allow us to update how our django forms look.
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs= {'class': 'form-control', 
            'placeholder': 'Email'
            }
        ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs= {'class': 'form-control',
            'placeholder': 'Password'
            }
    ))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs= {'class': 'form-control',
            'placeholder': 'Password Confirmation'
            }
    ))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        
        widgets = {
            'first_name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Last Name'}),
        }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ContractorSignupProfileForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ('main_instrument',)
    
    # Field is not required.
    def __init__(self, *args, **kwargs):
        super(ContractorSignupProfileForm, self).__init__(*args, **kwargs)
        self.fields['main_instrument'].required = False


class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs= {'class': 'form-control'}
        ))
    password = None # Hides password field

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

        widgets = {
            'first_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs= {'class': 'form-control'}),
        }

class UserContractorEditDetailsForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = (
            'profile_picture', 
            'phone_number',
            'main_instrument',
            'city',
            'public_liability',
            'pa_system',
            'battery_amp',
            'alumni',
            'year_finished', 
            )