from django.urls import path
from . import views

urlpatterns = [
    path("<int:event_id>", views.worksheet_view, name='worksheet_view')
]