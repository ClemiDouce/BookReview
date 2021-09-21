from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from ticket.models import Ticket


class ListTicketView(ListView):
    model = Ticket
    template_name = 'ticket/list-ticket.html'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

class CreateTicketView(CreateView):
    model = Ticket
    template_name = 'ticket/create-ticket.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('ticket:ticket-index')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        return super().form_valid(form)

class DeleteTicketView(DeleteView):
    model = Ticket
    template_name = 'ticket/delete-ticket.html'
    success_url = reverse_lazy('ticket:ticket-index')

class UpdateTicketView(UpdateView):
    model = Ticket
    template_name = 'ticket/update-ticket.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('ticket:ticket-index')