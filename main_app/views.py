from django.shortcuts import render
from .models import Service, Contact

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service_index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})