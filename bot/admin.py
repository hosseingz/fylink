from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(BotUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'username', 'traffic', 'wallet', 'start_time']
    list_per_page = 10
    list_filter = ['start_time']
    search_fields = ['chat_id', 'username']
    date_hierarchy = 'start_time'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'purchase_date', 'duration']
    list_per_page = 10
    search_fields = ['user']
    date_hierarchy = 'purchase_date'
    raw_id_fields = ['user']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'method', 'is_active']
    list_per_page = 10
    list_filter = ['method', 'is_active']
    search_fields = ['address']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'currency', 'date', 'source_address', 'destination_address']
    list_per_page = 10
    list_filter = ['currency', 'date', 'destination_address']
    search_fields = ['user', 'source_address']
    date_hierarchy = 'date'
    raw_id_fields = ['user', 'destination_address']


@admin.register(Hard)
class HardAdmin(admin.ModelAdmin):
    list_display = ['host', 'ftp_u', 'space', 'usage', 'is_active']
    list_per_page = 10
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['host']


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ['date', 'new_users', 'traffic']
    list_per_page = 30
    list_filter = ['date']
    date_hierarchy = 'date'


@admin.register(MonthlyReport)
class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ['month', 'new_users', 'traffic']
    list_per_page = 12
    search_fields = ['month']
    date_hierarchy = 'month'
