from django.urls import path

from . import views

urlpatterns = [
    path("bookers_home_view", views.bookers_home_view, name="bookers_home_view"),
    path("create_new_event", views.create_new_event, name="create_new_event"),
    path("", views.bookers_home_view, name="bookers_home_view"),
    path("bookers_details", views.bookers_details, name="bookers_details"),
    path("bookers_gig_history", views.bookers_gig_history, name="bookers_gig_history"),
    path("bookers_gig_history/<int:event_pk>", views.bookers_undo_complete_event, name="bookers_undo_complete_event"),
    path("bookers_clients_view", views.bookers_clients_view, name="bookers_clients_view"),    
    path("bookers_edit_clients/<int:client_id>", views.bookers_edit_clients_view, name="bookers_edit_clients_view"),
    path("bookers_create_new_client/", views.bookers_create_new_client, name="bookers_create_new_client"),
    path("bookers_musicians_view/", views.bookers_musicians_view, name="bookers_musicians_view"),
    path("bookers_musicians_view/<int:event_musician_pk>", views.bookers_musicians_view, name="bookers_musicians_view"),
]