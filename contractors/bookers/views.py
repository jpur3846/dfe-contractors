from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from events.forms import EventCreationForm
from clients.models import Client
from clients.forms import ClientEditForm, ClientCreationForm
from .forms import BookerEditDetailsForm
from users.forms import UserEditForm

def bookers_clients_view(request):
    context = {
        'clients': Client.objects.all(),
        'client_creation_form': ClientCreationForm,
        }

    return render(request, 'bookers/bookers_clients.html', context)

def bookers_edit_clients_view(request, client_id):
    client = Client.objects.get(pk=client_id)

    if request.method == "POST":
        form = ClientEditForm(request.POST, instance=client)

        if form.is_valid() and 'save_changes' in request.POST:
            form.save()
        elif form.is_valid() and 'delete_client' in request.POST:
            client.delete()
            messages.add_message(request, messages.SUCCESS, 'Client successfully deleted')
            return HttpResponseRedirect(reverse('bookers_clients_view'))


    context = {
        'client': client,
        'form': ClientEditForm(instance=client)
    }
    
    return render(request, 'bookers/bookers_edit_clients.html', context)

def bookers_create_new_client(request):
    if request.method == 'POST':
        new_client_form = ClientCreationForm(request.POST)

        if new_client_form.is_valid():
            new_client_form.save()

    context = {
        'clients': Client.objects.all(),
        'client_creation_form': ClientCreationForm,
        }

    return render(request, 'bookers/bookers_clients.html', context)
    
def create_new_event(request):
    if request.method == 'POST':
        new_event_form = EventCreationForm(request.POST)
        
        if new_event_form.is_valid():
            new_event = new_event_form.save(commit=False)
            new_event.booker = request.user.booker
            new_event.save()
        
    context = {
        'events': request.user.booker.events.all(),
        'event_creation_form': EventCreationForm
    }

    return render(request, 'bookers/bookers_home_view.html', context)

def bookers_home_view(request):

    context = {
        'events': request.user.booker.events.all(),
        'event_creation_form': EventCreationForm
    }
    return render(request, 'bookers/bookers_home_view.html', context)

def bookers_details(request):
    """
    Page to update and edit user details.
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        booker_form = BookerEditDetailsForm(request.POST, request.FILES, instance=request.user.booker)

        if form.is_valid() and booker_form.is_valid():
            user = form.save()
            booker = booker_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile successfully updated')
            return HttpResponseRedirect(reverse('bookers_home_view'))

        else:
            messages.add_message(request, messages.ERROR, 'Profile has not been updated')
            context = {'form': form, 'booker_form': booker_form}
            return render(request, 'bookers_details.html', context)
    
    context = {
        'form': UserEditForm(instance=request.user),
        'booker_form': BookerEditDetailsForm(instance=request.user.booker)
    }
    return render(request, 'bookers/bookers_details.html', context)

def bookers_gig_history(request):
    context = {
        'events': request.user.booker.events.all()
    }
    return render(request, 'bookers/bookers_gig_history.html', context)