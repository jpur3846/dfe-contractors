from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Event
from .utils import render_to_pdf
from .forms import EventEditForm

def edit_event_view(request, event_id):
    """
    Edit event and save changes.
    """
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form =  EventEditForm(request.POST, instance=event)

        if form.is_valid() and 'save_changes' in request.POST:
            form.save()
        elif form.is_valid() and 'delete_event' in request.POST:
            event.delete()
            messages.add_message(request, messages.SUCCESS, 'Event successfully deleted')
            return HttpResponseRedirect(reverse('bookers_home_view'))

    context = {
            'event': event,
            'event_edit_form': EventEditForm(instance=event)
        }
    return render(request, "events/edit_event.html", context)

def worksheet_view(request, event_id):
    """
    View auto generated worksheet as a contractor
    """
    event = Event.objects.get(pk=event_id)
    context = {
            'event': event.__dict__.items() # Getting all data.
        }
    return render(request, "events/contractor_worksheet.html", context)

def generate_pdf_invoice(request, event_id, *args, **kwargs):
    """
    When click to send an invoice it generates one.
    for force download visit https://www.youtube.com/watch?v=B7EIK9yVtGY
    """
    event = Event.objects.get(pk=event_id)

    template = get_template('pdf/contractor_invoice.html')
    context = {'event': event, 'user': request.user}
    html = template.render(context)
    pdf = render_to_pdf('pdf/contractor_invoice.html', context)

    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponseRedirect(reverse('worksheet_view'))