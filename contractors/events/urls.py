from django.urls import path
from . import views

urlpatterns = [
    path("<int:event_id>", views.worksheet_view, name='worksheet_view'),
    path("invoice/<int:event_id>", views.generate_pdf_invoice, name='generate_pdf_invoice'),
    path("invoice/send/<int:event_id>", views.generate_and_send_pdf_invoice, name='generate_and_send_pdf_invoice'),
    path("email_invite_musician/<int:event_id>/<int:eventmusician_id>", views.email_invite_musician, name='email_invite_musician'),
    path("email_worksheet_reminder/<int:event_id>", views.email_worksheet_reminder, name='email_worksheet_reminder'),
    path("edit_event_view/<int:event_id>", views.edit_event_view, name='edit_event_view'),
    path("edit_event_view/confirm_delete_event/<int:event_id>", views.confirm_delete_event, name='confirm_delete_event'),
    path("edit_event_view/<int:event_id>/edit_event_musicians_view/<int:musician_id>",
    views.edit_event_musicians_view, name='edit_event_musicians_view'),
]