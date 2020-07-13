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
from datetime import datetime

# My imports
from .forms import (
    SignupForm, 
    ContractorSignupProfileForm, 
    UserEditForm, 
    UserContractorEditDetailsForm
)
from .models import Contractor

# Default landing page.
def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))
    return render(request, 'users/user_home.html', {
        'events': (request.user.contractor.events.filter(date__gte=datetime.now())),
        'user': request.user
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
            user = form.save()
            profile_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile successfully updated')
            context = {'form': form, 'profile_form': profile_form}
            return render(request, 'users/user_details.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Profile has not been updated')
            context = {'form': form, 'profile_form': profile_form}
            return render(request, 'users/user_details.html', context)

    else:
        form = UserEditForm(instance=request.user)
        profile_form = UserContractorEditDetailsForm(instance=request.user.contractor) # Instance pre populates the form.
        context = {'form': form, 'profile_form': profile_form}

    return render(request, 'users/user_details.html', context)

def user_event_history(request):
    context = {
        'past_events': (request.user.contractor.events.filter(date__lte=datetime.now()))
    }
    return render(request, 'users/user_event_history.html', context)

def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password) # No username. Username and email are same.

        if user is not None:
            login(request, user)
            banner = 'You have successfully logged in. Welcome!' # we can add some user banners here if we needed.
            messages.add_message(request, messages.SUCCESS, banner) 
            return HttpResponseRedirect(reverse("user_home"))
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return render(request, "users/signin.html")

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
            messages.add_message(request, messages.SUCCESS, 'You have signed up!')
            context = {'form': form}
            return render(request, "users/signup.html", context)
        
    else:
        form = SignupForm()
        contractor_form = ContractorSignupProfileForm()
        
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def signout_view(request):
    logout(request)
    
    messages.add_message(request, messages.SUCCESS, "You have successfully signed out!")
    return render(request, "users/signin.html")

def contact_view(request):
    return render(request, "users/contact.html", {'user': request.user})