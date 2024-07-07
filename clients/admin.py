from django.contrib import admin

from clients.models import Client


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comments', 'owner')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email', 'owner')