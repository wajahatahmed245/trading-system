from django.contrib import admin

# Register your models here.
from trading.models import TradingUser, AccountSize, Broker, Subject, VideoLink, MonthlyStatistic, Status

admin.site.register(TradingUser)
admin.site.register(AccountSize)
admin.site.register(Broker)
admin.site.register(VideoLink)
admin.site.register(Subject)
admin.site.register(MonthlyStatistic)
admin.site.register(Status)