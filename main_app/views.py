from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Service:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

services = [
    Service('Product 1', 'Description for product 1', 10.00),
    Service('Product 2', 'Description for product 2', 20.00),
    Service('Product 3', 'Description for product 3', 30.00),
]

class Contact: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

contacts = [
    Contact('Steve', 'americasass@gmail.com', '123-456-7890'),
]

def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service_index(request):
    return render(request, 'services/index.html', {'services': services})

def contact(request):
    return render(request, 'contact.html', {'contacts': contacts})