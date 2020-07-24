from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from . import views

urlpatterns = [
    path("", views.signin_view, name="signin"),
    path("user_home", views.user_home, name="user_home"),
    path("user_home/<int:eventmusician_pk>", views.user_accept_decline_gig, name="user_accept_decline_gig"),
    path("user_details", views.user_details, name="user_details"),
    path("user_event_history", views.user_event_history, name="user_event_history"),
    path("signin", views.signin_view, name="signin"),
    path("signup", views.signup_view, name="signup"),
    path("contact", views.contact_view, name="contact"),
    path("signout", views.signout_view, name="signout"),
    path("reset-password", PasswordResetView.as_view(template_name='users/reset_password/reset_password.html'), name='password_reset'),
    path("reset-password/done", PasswordResetDoneView.as_view(template_name='users/reset_password/reset_password_done.html'), name="password_reset_done"),
    path("reset-password/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='users/reset_password/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='users/reset_password/reset_password_complete.html'), name='password_reset_complete'),
]