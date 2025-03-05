from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service_index(request):
    return render(request, 'services/index.html', {'services': services})

def contact(request):
    return render(request, 'contact.html', {'contacts': contacts})