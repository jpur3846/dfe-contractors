from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin_view, name="signin"),
    path("user_home", views.user_home, name="user_home"),
    path("user_details", views.user_details, name="user_details"),
    path("signin", views.signin_view, name="signin"),
    path("signup", views.signup_view, name="signup"),
    path("contact", views.contact_view, name="contact"),
    path("signout", views.signout_view, name="signout")
]