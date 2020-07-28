from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from events.models import Event

# Create your views here.

def con_staff_view(request):
    context = {
        'events': Event.objects.filter(gig_source='usyd')
    }
    return render(request, 'con/con_staff_view.html', context)

def con_event_details_view(request, event_id):
    event = Event.objects.get(pk=event_id)

    context = {
        'event': event,
        'musicians': event.eventmusicians_set.all(),
    }

    return render(request, 'con/con_event_details_view.html', context)