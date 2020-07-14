from django.urls import path

from . import views

urlpatterns = [
    path("", views.con_staff_view, name="con_staff_view"),
    path("con_staff_view", views.con_staff_view, name="con_staff_view")
]