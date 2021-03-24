from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'trading/index.html')


def register(request):
    return render(request, 'trading/register.html')


def contact(request):
    return render(request, 'trading/contact.html')
