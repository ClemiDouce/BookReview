from django.contrib import admin

# Register your models here.
from ticket.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'user'
    )