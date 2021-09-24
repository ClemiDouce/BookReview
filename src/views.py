from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from follows.models import UserFollows
from review.models import Review
from ticket.models import Ticket


class FluxView(TemplateView):
    template_name = 'website/flux.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followed = [follow.followed_user for follow in UserFollows.objects.filter(user=self.request.user)]
        critics = Review.objects.filter(user__in=[*followed, self.request.user]).order_by('-time_created')
        context["tickets"] = Ticket.objects.filter(user__in=[*followed, self.request.user]).order_by('-time_created')
        context["reviews"] = critics
        context["already_critic"] = [critic.ticket for critic in critics]
        return context

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')


class PostsView(TemplateView):
    template_name = "website/posts.html"

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data()
        user_tickets = Ticket.objects.filter(user=self.request.user)
        user_reviews = Review.objects.filter(user=self.request.user)
        all_posts = [*user_tickets, *user_reviews]
        all_posts.sort(key=lambda post: post.time_created, reverse=True)
        context['all_posts'] = all_posts
        return context
