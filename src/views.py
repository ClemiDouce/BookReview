from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from follows.models import UserFollows
from review.models import Review
from src.forms import SignupForm
from ticket.models import Ticket


class FluxView(TemplateView):
    template_name = 'website/flux.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followed = [follow.followed_user for follow in UserFollows.objects.filter(user=self.request.user)]
        all_reviews = Review.objects.filter(user__in=[*followed, self.request.user])
        all_tickets = Ticket.objects.filter(user__in=[*followed, self.request.user])
        all_posts = sorted([*all_reviews, *all_tickets], key=lambda post: post.time_created, reverse=True)
        context['all_posts'] = all_posts
        context["already_critic"] = [critic.ticket for critic in all_reviews.filter(user=self.request.user)]
        return context


class SignupView(CreateView):
    form_class = SignupForm
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
        context["already_critic"] = [critic.ticket for critic in user_reviews]
        return context
