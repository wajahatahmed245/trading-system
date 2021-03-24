from django.contrib import admin

# Register your models here.
from trading.models import TradingUser, AccountSize, Broker

admin.site.register(TradingUser)
admin.site.register(AccountSize)
admin.site.register(Broker)