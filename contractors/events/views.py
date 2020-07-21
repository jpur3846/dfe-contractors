from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Event, EventMusicians
from .utils import render_to_pdf
from .forms import EventEditForm, EditEventMusician, AddEventMusician
from users.models import Contractor

def edit_event_view(request, event_id):
    """
    Edit event and save changes.
    """
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventEditForm(request.POST, request.FILES, instance=event)
        add_musician = AddEventMusician(request.POST)

        if form.is_valid() and 'save_changes' in request.POST:
            form.save()

        elif form.is_valid() and 'delete_event' in request.POST:
            event.delete()
            messages.add_message(request, messages.SUCCESS, 'Event successfully deleted')
            return HttpResponseRedirect(reverse('bookers_home_view'))
        
        elif form.is_valid() and 'add_musician' in request.POST:
            musician_id = request.POST['contractor']

            if Contractor.objects.get(pk=musician_id) not in event.musicians.all():
                event.musicians.add(request.POST['contractor'])
                messages.add_message(request, messages.SUCCESS, 'Musician successfully added')
            
            else:
                messages.add_message(request, messages.ERROR, 'Musician already added to event')
            
    context = {
            'event': event,
            'musicians': event.musicians.all(),
            'event_edit_form': EventEditForm(instance=event),
            'add_event_musician': AddEventMusician(),
        }
    return render(request, "events/edit_event.html", context)

def edit_event_musicians_view(request, musician_id, event_id):
    event = Event.objects.get(pk=event_id)
    contractor = Contractor.objects.get(pk=musician_id)
    musician = EventMusicians.objects.filter(contractor=contractor, event=event).first()

    context = {
        'event': event,
        'musician': musician,
        'event_musicians_edit_form': EditEventMusician(instance=musician)
    }

    if request.method == 'POST':
        form = EditEventMusician(request.POST, instance=musician)

        if form.is_valid() and 'save_changes' in request.POST:
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Changes successfully saved')
            return HttpResponseRedirect(reverse('edit_event_musicians_view', args=(event_id, musician_id, )))

        elif form.is_valid() and 'delete_musician' in request.POST:
            musician.delete()
            messages.add_message(request, messages.SUCCESS, 'Musician successfully deleted')
            return HttpResponseRedirect(reverse('edit_event_view', args=(event_id,)))

        else:
            messages.add_message(request, messages.ERROR, 'Changes Invalid')
            return HttpResponseRedirect(reverse('edit_event_musicians_view', args=(event_id, musician_id, )))

    return render(request, "events/edit_event_musicians.html", context)

def worksheet_view(request, event_id):
    """
    View auto generated worksheet as a contractor.
    The event_id is an EventMusician object
    """
    event = EventMusicians.objects.get(pk=event_id)
    bandleader = None
    musicians = event.event.eventmusicians_set.all() # Need to get a set of musicians.

    for musician in musicians:
        if musician.is_bandleader:
            bandleader = musician

    context = {
            'event': event,
            'bandleader': bandleader,
            'musicians': musicians
        }
    return render(request, "events/contractor_worksheet.html", context)

def generate_pdf_invoice(request, event_id, *args, **kwargs):
    """
    When click to send an invoice it generates one.
    for force download visit https://www.youtube.com/watch?v=B7EIK9yVtGY
    """
    event = EventMusicians.objects.get(pk=event_id)

    template = get_template('pdf/contractor_invoice.html')
    context = {'event': event, 'user': request.user}
    html = template.render(context)
    pdf = render_to_pdf('pdf/contractor_invoice.html', context)

    requirements = [
        request.user.contractor.gst_status,
        request.user.contractor.abn,
        request.user.contractor.account_name,
        request.user.contractor.bsb,
        request.user.contractor.account_number,
    ]
    for requirement in requirements:
        if requirement == None:
            messages.add_message(request, messages.ERROR, 'Banking details incomplete')
            return HttpResponseRedirect(reverse('user_home'))

    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponseRedirect(reverse('worksheet_view'))