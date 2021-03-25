from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

from trading.models import Broker, Subject
from trading.models import AccountSize
from trading.models import TradingUser

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate


def create_builtin_user(mail, password, name):
    try:
        user = User.objects.create_user(username=mail, email=mail, password=password)
        user.first_name = name
        user.save()
        return user
    except Exception as error_message:
        raise ModuleNotFoundError(str(error_message))


def validate_password(password, confirm_password):
    password_match = password == confirm_password
    if not password_match:
        raise ModuleNotFoundError("password are not matched")


def make_user(request_obj):
    mail = request_obj.POST.get('mail')
    name = request_obj.POST.get('name')
    phone = request_obj.POST.get('phone')
    password = request_obj.POST.get('password')
    confirmPassword = request_obj.POST.get('confirmPassword')
    validate_password(password=password, confirm_password=confirmPassword)
    broker = int(request_obj.POST.get('broker'))
    account = int(request_obj.POST.get('account'))
    broker_obj = Broker.objects.get(pk=broker)
    account_size_obj = AccountSize.objects.get(pk=account)
    user = create_builtin_user(mail=mail, password=password, name=name)
    trading_user = TradingUser(user=user, broker=broker_obj, phone_number=phone, account_size=account_size_obj)
    trading_user.save()


def index(request):
    return render(request, 'trading/index.html')


def register(request):
    all_brokers = Broker.objects.all()
    all_account_size = AccountSize.objects.all()
    context = {'broker': all_brokers, "all_account_size": all_account_size}

    if request.POST:
        try:
            make_user(request_obj=request)
            context.update({"alert": 'registered succefully'})

        except Exception as error_message:
            context.update({"alert": str(error_message)})
            return render(request, 'trading/register.html', context=context)

    return render(request, 'trading/register.html', context=context)


def contact(request):
    return render(request, 'trading/contact.html')


@login_required(login_url='index')
def home(request):
    user = request.user
    user_details = Subject.objects.filter(user__user=user).all()
    context = dict(user=user, data_details=user_details)
    return render(request, 'trading/home.html', context=context)


def log_in(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.session['error']:
                del request.session['error']
            return redirect('home')

        else:
            request.session['error'] = "Wrong credentials try again"
            return redirect('index')
    return render(request, 'trading/contact.html')


def logout_page(request):
    logout(request)
    return render(request, 'trading/index.html')

def faq(request):
    return render(request, 'trading/faq.html')
