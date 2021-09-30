from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView

from review.forms import CreateReviewForm
from review.models import Review
from ticket.forms import CreateTicketForm
from ticket.models import Ticket


class ListReviewView(ListView):
    model = Review
    template_name = 'review/list-review.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CreateReviewView(CreateView):
    model = Review
    template_name = 'review/create-review.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('ticket:ticket-index')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        return super().form_valid(form)


class CreateReviewAndTicket(TemplateView):
    template_name = 'review/review-and-ticket.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_form'] = CreateTicketForm(prefix="ticket-form")
        context['review_form'] = CreateReviewForm(prefix="review-form")
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ticket_form = CreateTicketForm(request.POST, request.FILES, prefix='ticket-form')
        review_form = CreateReviewForm(request.POST, prefix='review-form')
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            ticket.user = request.user
            ticket.save()
            review.save()
            return redirect(reverse('flux'))
        else:
            return render(request, self.template_name, {
                'ticket-form': ticket_form,
                'review-form': review_form
            })


class CreateReviewOnTicketView(CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = "review/review-on-ticket.html"
    success_url = reverse_lazy('flux')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ticket_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = Ticket.objects.get(pk=self.kwargs.get('pk'))
        context['ticket'] = ticket
        return context


class DeleteReviewView(DeleteView):
    model = Review
    template_name = 'review/delete-review.html'
    success_url = reverse_lazy('posts')


class UpdateReviewView(UpdateView):
    model = Review
    template_name = 'review/update-review.html'
    fields = ['headline', 'body', 'rating']
    success_url = reverse_lazy('posts')
