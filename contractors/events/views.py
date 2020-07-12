from django.shortcuts import render
from .models import Event

def worksheet_view(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {
            'event': event
        }
    return render(request, "events/contractor_worksheet.html", context)