from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from trading.models import Broker, AccountSize


def make_user(request_obj):
    mail = request_obj.POST.get('mail')
    phone = request_obj.POST.get('phone')
    password = request_obj.POST.get('password')
    confirmPassword = request_obj.POST.get('confirmPassword')
    broker = request_obj.POST.get('broker')
    account = request_obj.POST.get('account')


def index(request):
    return render(request, 'trading/index.html')


def register(request):
    print()
    if request.POST:
        print()
    all_brokers = Broker.objects.all()
    all_account_size = AccountSize.objects.all()

    context = {'broker': all_brokers, "all_account_size": all_account_size}
    return render(request, 'trading/register.html', context=context)


def contact(request):
    return render(request, 'trading/contact.html')
