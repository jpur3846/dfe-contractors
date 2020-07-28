from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage

import datetime
from smtplib import SMTPException

from .models import Event, EventMusicians
from .utils import render_to_pdf
from .forms import EventEditForm, EditEventMusician, AddEventMusician
from users.models import Contractor

@login_required
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
            messages.add_message(request, messages.SUCCESS, 'Event successfully updated')

        elif form.is_valid() and 'delete_event' in request.POST:
            # Confirm event deletion.
            return HttpResponseRedirect(reverse('confirm_delete_event', args=(event_id, )))
        
        elif add_musician.is_valid() and 'add_musician' in request.POST:
            musician_id = request.POST['contractor']

            # Can't add musos to expired events.
            if event.date < datetime.date.today():
                messages.add_message(request, messages.ERROR, 'Cannot add musicians to past events')

            elif Contractor.objects.get(pk=musician_id).denylisted:
                messages.add_message(request, messages.ERROR, 'This musician has been denylisted!')

            # Add muso if they are not added
            elif Contractor.objects.get(pk=musician_id) not in event.musicians.all():
                event.musicians.add(request.POST['contractor'])
                name = Contractor.objects.get(pk=musician_id).user.first_name
                messages.add_message(request, messages.SUCCESS, f'{name} successfully added')
            
            else:
                messages.add_message(request, messages.ERROR, 'Musician already added to event')

        else:
            messages.add_message(request, messages.ERROR, 'Event NOT updated')
            
    context = {
            'event': event,
            'musicians': event.eventmusicians_set.all(),
            # Musos that decline are stored as a Comma Separated List.
            'unavailable_musicians': set(event.unavailable_musicians.split(',')),
            'event_edit_form': EventEditForm(instance=event),
            'add_event_musician': AddEventMusician(),
        }
    return render(request, "events/edit_event.html", context)

@login_required
def confirm_delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        if 'confirm' in request.POST:      
            event.delete()
            messages.add_message(request, messages.SUCCESS, 'Event successfully deleted')
            return HttpResponseRedirect(reverse('bookers_home_view'))
        else:
            return HttpResponseRedirect(reverse('edit_event_view', args=(event_id, )))

    return render(request, "events/confirm_delete_event.html")

@login_required
def email_invite_musician(request, eventmusician_id, event_id=None):
    """
    Musician specific invite for an event.
    """
    musician = EventMusicians.objects.get(pk=eventmusician_id)

    send_mail(
        'You have been invited to do a gig!',
        'Please visit our site to accept/decline this gig.',
        'info@danielfrancis.com.au',
        [musician.contractor.user.email],
        fail_silently=False,
    )

    musician.email_invite_sent = True
    musician.save()
    messages.add_message(request, messages.SUCCESS, 'Invite successfully sent!')
    
    return HttpResponseRedirect(reverse('edit_event_view', args=(event_id, )))

@login_required
def email_worksheet_reminder(request, event_id):
    """
    Generic worksheet reminder for all musicians.
    """
    event = Event.objects.get(pk=event_id)

    send_mail(
        'Worksheet reminder',
        'Please visit our site to see info on this gig.',
        'info@danielfrancis.com.au',
        event.get_musicians_emails(),
        fail_silently=False,
    )

    event.email_worksheet_reminder = True
    event.save()
    messages.add_message(request, messages.SUCCESS, 'Reminder worksheet successfully sent!')
    
    return HttpResponseRedirect(reverse('edit_event_view', args=(event_id, )))

@login_required
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

        elif 'delete_musician' in request.POST:
            musician.delete()
            messages.add_message(request, messages.SUCCESS, 'Musician successfully deleted')
            return HttpResponseRedirect(reverse('edit_event_view', args=(event_id,)))

        else:
            messages.add_message(request, messages.ERROR, 'Changes Invalid')
            return HttpResponseRedirect(reverse('edit_event_musicians_view', args=(event_id, musician_id, )))

    return render(request, "events/edit_event_musicians.html", context)

@login_required
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

@login_required
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

@login_required
def generate_and_send_pdf_invoice(request, event_id, *args, **kwargs):
    # Event is an eventmusicians object
    event = EventMusicians.objects.get(pk=event_id)

    template = get_template('pdf/contractor_invoice.html')
    context = {'event': event, 'user': request.user}
    html = template.render(context)
    pdf = render_to_pdf('pdf/contractor_invoice.html', context)

    email = EmailMessage(
    f'Invoice for event on {event.event.date} from {event.contractor.user.first_name} {event.contractor.user.last_name}',
    'Invoice for event',
    'info@danielfrancis.com.au',
    ['info@danielfrancis.com.au', event.contractor.user.email],
    reply_to=['info@danielfrancis.com.au'],
    )
    
    try:
        email.send(fail_silently=False)
        email.attach(html, 'text/html')

        # This person has invoiced
        event.invoice_status = 'yes'
        event.save()

        messages.add_message(request, messages.SUCCESS, 'Email sent!')

    except SMTPException:
        messages.add_message(request, messages.ERROR, 'Email failed to send!')

    return HttpResponseRedirect(reverse('user_home'))