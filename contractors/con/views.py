from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def con_staff_view(request):
    return render(request, 'con/con_staff_view.html')