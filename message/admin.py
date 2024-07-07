from django.contrib import admin

from message.models import Message


# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'message', 'owner')
    list_filter = ('owner',)
    search_fields = ('subject', 'message')