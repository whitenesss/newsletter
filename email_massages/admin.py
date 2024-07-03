from django.contrib import admin

from email_massages.models import EmailMessage


# Register your models here.

@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'status', 'periodicity', 'start_date', 'end_date', 'next_send_time',
        'message',
        'owner')
    list_filter = (
        'periodicity', 'status', 'start_date', 'end_date', 'clients', 'message', 'owner'
    )
    search_fields = ('name', 'description', 'clients__name', 'message__subject')