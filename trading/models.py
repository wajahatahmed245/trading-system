from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class VideoLink(models.Model):
    video_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.video_link


class Broker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccountSize(models.Model):
    size = models.CharField(max_length=500)

    def __str__(self):
        return self.size


class TradingUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    account_size = models.ForeignKey(AccountSize, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


class Subject(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(TradingUser, on_delete=models.CASCADE)
    video_link = models.ManyToManyField(VideoLink)
