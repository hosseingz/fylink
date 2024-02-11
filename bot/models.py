from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.


class BotUser(models.Model):
    chat_id = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    traffic = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)

    start_time = models.DateTimeField(auto_now_add=True)
    # language = None

    def __str__(self):
        return f'{self.chat_id}'

    class Meta:
        ordering = ['chat_id']

        indexes = [
            models.Index(fields=['chat_id'])
        ]


class Subscription(models.Model):
    user = models.OneToOneField(BotUser, on_delete=models.CASCADE, related_name='subscription')
    purchase_date = models.DateTimeField(default=timezone.now)
    duration = models.DateField()

    def __str__(self):
        return f'{self.user.chat_id}'

    class Meta:
        ordering = ['-purchase_date']

        indexes = [
            models.Index(fields=['-purchase_date'])
        ]


class Address(models.Model):
    class Method(models.TextChoices):
        CART = 'CR', 'Cart'
        BITCOIN = "BTC", 'Bitcoin'
        TRON = "TRX", "Tron"
        LITECOIN = "LTC", 'Litecoin'

    address = models.CharField(max_length=250)
    method = models.CharField(max_length=3, choices=Method.choices)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.method}-{self.address[:5]}...'

    class Meta:
        ordering = ['address', 'is_active']

        indexes = [
            models.Index(fields=['address', 'is_active'])
        ]


class Transaction(models.Model):
    class Currency(models.TextChoices):
        TOMAN = 'TM', 'Toman'
        BITCOIN = "BTC", 'Bitcoin'
        TRON = "TRX", "Tron"
        LITECOIN = "LTC", 'Litecoin'

    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='transactions')
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, choices=Currency.choices)
    date = models.DateTimeField(default=timezone.now)

    source_address = models.CharField(max_length=250)
    destination_address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='transactions')

    def __str__(self):
        return f'{self.user.chat_id}'

    class Meta:
        ordering = ['-date']

        indexes = [
            models.Index(fields=['-date'])
        ]


class Hard(models.Model):
    host = models.CharField(max_length=100)
    ftp_u = models.CharField(max_length=250)
    ftp_p = models.CharField(max_length=250)
    space = models.PositiveIntegerField()
    usage = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.host


class DailyReport(models.Model):
    date = models.DateField(default=timezone.now().replace(hour=0, minute=0, second=0))
    new_users = models.PositiveIntegerField(default=0)
    traffic = models.PositiveIntegerField(default=0)


# class Tickets(models.Model):
#     report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, related_name='tickets')
#     user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='tickets')
#     message = models.TextField()


class MonthlyReport(models.Model):
    month = models.DateField()
    new_users = models.PositiveIntegerField(default=0)
    traffic = models.PositiveIntegerField(default=0)


class File(models.Model):
    file_id = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    file_extension = models.CharField(max_length=5)
    file_path = models.TextField()
    file_size = models.PositiveIntegerField()
    url = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file_name}{self.file_extension}"


class DownloadList(models.Model):
    chat_id = models.CharField(max_length=250)
    file = models.ForeignKey(File, on_delete=models.CASCADE)