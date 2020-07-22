# From Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Error Handling
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Other imports
import datetime

# My imports
from .forms import (
    SignupForm, 
    ContractorSignupProfileForm, 
    UserEditForm, 
    UserContractorEditDetailsForm
)
from .models import Contractor
from events.models import EventMusicians

# Default landing page.
def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))

    contractor = request.user.contractor

    events = EventMusicians.objects.filter(contractor=contractor)
    # Returns a query set of EventMusicians objects that we can then get
    # The details from. See EventMusician model for more.
    new_events = []
    
    for event in events:
        if event.event.date > datetime.date.today():
            new_events.append(event)

    return render(request, 'users/user_home.html', {
        'events': new_events
    })

def user_details(request):
    """
    Page to update and edit user details.
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        # request.FILES to allow profile pic upload
        profile_form = UserContractorEditDetailsForm(request.POST, request.FILES, instance=request.user.contractor)

        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            profile_form.save()

            user.username = request.POST['email'] # Username == to email
            user.save()

            messages.add_message(request, messages.SUCCESS, 'Profile successfully updated')
            context = {'form': form, 'profile_form': profile_form}
            return HttpResponseRedirect(reverse('user_details'))

        else:
            context = {'form': form, 'profile_form': profile_form}
            return render(request, 'users/user_details.html', context)

    else:
        form = UserEditForm(instance=request.user)
        profile_form = UserContractorEditDetailsForm(instance=request.user.contractor) # Instance pre populates the form.
        context = {'form': form, 'profile_form': profile_form}

    return render(request, 'users/user_details.html', context)

def user_event_history(request):
    contractor = request.user.contractor
    events = EventMusicians.objects.filter(contractor=contractor)
    past_events = []

    for event in events:
        if event.event.date < datetime.date.today():
            past_events.append(event)

    context = {
        'past_events': past_events
    }
    return render(request, 'users/user_event_history.html', context)

def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password) # No username. Username and email are same.

        if user is not None:
            if hasattr(user, 'contractor'): # Does the user have a contractor? 
                login(request, user)
                banner = f'Hey {user.first_name}! Welcome' # we can add some user banners here if we needed.
                messages.add_message(request, messages.SUCCESS, banner) 
                return HttpResponseRedirect(reverse("user_home"))

            elif hasattr(user, 'constaff'):
                login(request, user)
                banner = f'You have successfully logged in as a Con staff member. Welcome {user.first_name}!' # we can add some user banners here if we needed.
                messages.add_message(request, messages.SUCCESS, banner) 
                return HttpResponseRedirect(reverse("con_staff_view"))

            elif hasattr(user, 'booker'):
                login(request, user)
                banner = f'You have successfully logged in as a booking manager. Welcome {user.first_name}!' # we can add some user banners here if we needed.
                messages.add_message(request, messages.SUCCESS, banner) 
                return HttpResponseRedirect(reverse("bookers_home_view"))

        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return HttpResponseRedirect(reverse("signin"))

    return render(request, 'users/signin.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        contractor_form = ContractorSignupProfileForm(request.POST)

        if form.is_valid() and contractor_form.is_valid():
            
            try:
                user = form.save()
                contractor = contractor_form.save(commit=False) # Creates the contractor profile on user creation.
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'User already registered')
                context = {'form': form}
                return render(request, "users/signup.html", context)
            
            contractor.user = user
            contractor.save()

            messages.add_message(request, messages.SUCCESS, 'You have signed up!')
            return render(request, "users/signin.html")
        
        else:
            messages.add_message(request, messages.ERROR, 'Signup Failed')
            context = {'form': form}
            return render(request, "users/signup.html", context)
        
    else:
        form = SignupForm()
        contractor_form = ContractorSignupProfileForm()
        
    context = {'form': form, 'contractor_form': contractor_form}
    return render(request, 'users/signup.html', context)

def signout_view(request):
    logout(request)
    
    messages.add_message(request, messages.SUCCESS, "You have successfully signed out!")
    return render(request, "users/signin.html")

def contact_view(request):
    return render(request, "users/contact.html", {'user': request.user})