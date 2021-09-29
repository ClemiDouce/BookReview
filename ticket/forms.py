from django import forms
from django.forms import FileField, FileInput

from ticket.models import Ticket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        field_classes = {
            'image': FileField
        }
        widgets = {
            'image': FileInput
        }
