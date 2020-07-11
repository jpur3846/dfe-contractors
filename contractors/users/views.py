from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, ContractorProfileForm
from .models import Contractor

# Default landing page.
def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))
    return render(request, 'users/user_home.html', {
        'events': (request.user.contractor.events.all()),
        'user': request.user
    })

def user_details(request):
    return render(request, 'users/user_details.html')

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
        contractor_form = ContractorProfileForm(request.POST)

        if form.is_valid() and contractor_form.is_valid():
            user = form.save()
            contractor = contractor_form.save(commit=False) # Creates the contractor profile on user creation.

            contractor.user = user
            contractor.save()

            messages.add_message(request, messages.SUCCESS, 'You have signed up!')
            return render(request, "users/signin.html")
        
    else:
        form = SignupForm()
        contractor_form = ContractorProfileForm()
        
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def signout_view(request):
    logout(request)

    return render(request, "users/signin.html", {
        "message": "You have successfully signed out!"
    })

def contact_view(request):
    return render(request, "users/contact.html")