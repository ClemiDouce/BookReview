from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from ticket.forms import UpdateTicketForm
from ticket.models import Ticket


class CreateTicketView(CreateView):
    model = Ticket
    template_name = 'ticket/create-ticket.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('flux')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        return super().form_valid(form)


class DeleteTicketView(DeleteView):
    model = Ticket
    template_name = 'ticket/delete-ticket.html'
    success_url = reverse_lazy('posts')


class UpdateTicketView(UpdateView):
    model = Ticket
    form_class = UpdateTicketForm
    template_name = 'ticket/update-ticket.html'
    success_url = reverse_lazy('posts')
