
from django.http import HttpResponse  

from django.shortcuts import render, redirect

def dashboard_view(request):
    
    return render(request, 'control/dashboard.html')




