from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Event
from .utils import render_to_pdf

# Event Admin Views

def event_admin_home_view(request):
    return render(request, 'event_admin/event_admin_home_view.html')

# Contractor Views
def worksheet_view(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {
            'event': event
        }
    return render(request, "events/contractor_worksheet.html", context)

def generate_pdf_invoice(request, event_id, *args, **kwargs):
    """
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