from django.shortcuts import render

# Create your views here.

def con_staff_view(request):
    return render(request, 'con/con_staff_view.html')