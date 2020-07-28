from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from datetime import datetime

from events.forms import EventCreationForm
from events.models import EventMusicians, Event
from clients.models import Client
from clients.forms import ClientEditForm, ClientCreationForm
from .forms import BookerEditDetailsForm
from users.forms import UserEditForm
from users.models import Contractor

@login_required
def bookers_clients_view(request):
    context = {
        'clients': Client.objects.all(),
        'client_creation_form': ClientCreationForm,
        }

    return render(request, 'bookers/bookers_clients.html', context)

@login_required
def bookers_edit_clients_view(request, client_id):
    client = Client.objects.get(pk=client_id)

    if request.method == "POST":
        form = ClientEditForm(request.POST, instance=client)

        if form.is_valid() and 'save_changes' in request.POST:
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Client successfully updated')
            return HttpResponseRedirect(reverse('bookers_edit_clients_view', args=(client_id,)))

        elif form.is_valid() and 'delete_client' in request.POST:
            client.delete()
            messages.add_message(request, messages.SUCCESS, 'Client successfully deleted')
            return HttpResponseRedirect(reverse('bookers_clients_view'))


    context = {
        'client': client,
        'form': ClientEditForm(instance=client)
    }
    
    return render(request, 'bookers/bookers_edit_clients.html', context)

@login_required
def bookers_create_new_client(request):
    if request.method == 'POST':
        new_client_form = ClientCreationForm(request.POST)

        if new_client_form.is_valid():
            new_client_form.save()

    context = {
        'clients': Client.objects.all(),
        'client_creation_form': ClientCreationForm(),
        }

    return render(request, 'bookers/bookers_clients.html', context)

@login_required    
def create_new_event(request):
    if request.method == 'POST':
        new_event_form = EventCreationForm(request.POST)
        
        if new_event_form.is_valid():
            new_event = new_event_form.save(commit=False)
            new_event.booker = request.user.booker
            new_event.save()
            messages.add_message(request, messages.SUCCESS, 'Event successfully created!')
        else:
            # Parse out our errors to give back.
            error_dict = dict(new_event_form.errors)
            errors = ''

            for key in error_dict.keys():
                errors += error_dict[key].as_text()[2:]

            messages.add_message(request, messages.ERROR, 'Event failed to be added. ' + errors)

    return HttpResponseRedirect(reverse('bookers_home_view'))

@login_required
def bookers_home_view(request):
    upcoming_events = request.user.booker.events.filter(date__gte=datetime.today())
    past_events = request.user.booker.events.filter(date__lte=datetime.today())
    events_to_wrap_up = []

    for event in past_events:
        if event.is_complete() == False:
            events_to_wrap_up.append(event)

    context = {
        'events_to_wrap_up': events_to_wrap_up,
        'events': upcoming_events,
        'event_creation_form': EventCreationForm
    }
    return render(request, 'bookers/bookers_home_view.html', context)

@login_required
def bookers_details(request):
    """
    Page to update and edit user details.
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        booker_form = BookerEditDetailsForm(request.POST, request.FILES, instance=request.user.booker)

        if form.is_valid() and booker_form.is_valid():
            user = form.save(commit=False)
            booker = booker_form.save()

            user.username = request.POST['email'] # Update username == email
            user.save()

            messages.add_message(request, messages.SUCCESS, 'Profile successfully updated')
            return HttpResponseRedirect(reverse('bookers_details'))

        else:
            messages.add_message(request, messages.ERROR, 'Profile has not been updated')
            context = {'form': form, 'booker_form': booker_form}
            return render(request, 'bookers_details.html', context)
    
    context = {
        'form': UserEditForm(instance=request.user),
        'booker_form': BookerEditDetailsForm(instance=request.user.booker)
    }
    return render(request, 'bookers/bookers_details.html', context)

@login_required
def bookers_gig_history(request):
    events_ls = request.user.booker.events.filter(date__lte=datetime.today())
    past_events = []

    for event in events_ls:
        if event.is_complete():
            past_events.append(event)
        
    context = {
        'events': past_events
    }
    return render(request, 'bookers/bookers_gig_history.html', context)

@login_required
def bookers_musicians_view(request, event_musician_pk=None):
    """
    Post method marks the muso as being paid.
    """
    if request.method == 'POST':
        event_musician = EventMusicians.objects.get(pk=event_musician_pk)

        try:
            event_musician.payment_status = 'yes'
            event_musician.save()
            messages.add_message(request, messages.SUCCESS, 'Payment Recorded')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Payment has not been recorded')

    context = {
        'contractors': Contractor.objects.all(),
    }
    return render(request, 'bookers/bookers_musicians_details.html', context=context)

@login_required
def bookers_undo_complete_event(request, event_pk):
    event = Event.objects.get(pk=event_pk)

    try:
        event.event_complete = False
        event.save()
        messages.add_message(request, messages.SUCCESS, 'Event is now editable in booking screen')
    except IntegrityError:
        messages.add_message(request, messages.ERROR, 'Reversal failed')

    return HttpResponseRedirect(reverse('bookers_home_view'))