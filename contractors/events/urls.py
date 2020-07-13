from django.urls import path
from . import views

urlpatterns = [
    path("<int:event_id>", views.worksheet_view, name='worksheet_view'),
    path("invoice/<int:event_id>", views.generate_pdf_invoice, name='generate_pdf_invoice')
]