from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, ContractorProfileForm
from events.models import Event, Contractor

# Default landing page.
def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))
    return render(request, 'users/user_home.html', {
        'events': (request.user.contractor.events.all()),
        'user': request.user
    })

def signin_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user_home"))
        else:
            return render(request, "users/signin.html", {
                "message": "Invalid Credentials."
            })

    return render(request, 'users/signin.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        contractor_profile_form = ContractorProfileForm(request.POST)

        if form.is_valid() and contractor_profile_form.is_valid():
            user = form.save()
            profile = contractor_profile_form.save(commit=False) # won't save to db right away.
            profile.user = user # This hooks up our user to their contractor info.

            profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = request.POST['first_name'] # How do I post first name?
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return render(request, "users/signin.html", {
                "message": "You have successfully signed up!"
            })
        
    else:
        form = UserCreationForm()
        contractor_profile_form = ContractorProfileForm()
        
    context = {'form': form, 'contractor_profile_form': contractor_profile_form }
    return render(request, 'users/signup.html', context)

def signout_view(request):
    logout(request)

    return render(request, "users/signin.html", {
        "message": "You have successfully signed out!"
    })

def contact_view(request):
    return render(request, "users/contact.html")